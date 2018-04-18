#Análise Lexica
import re

class Dfa:
    def __init__(self, alfabeto, estadosFinais, automato, num_estados):
        self.alfabeto = alfabeto
        self.estadosFinais = estadosFinais
        self.automato = automato
        self.N = num_estados
        self.M = 300
        self.delta = []
        self.buildDelta()

    def initDelta(self):
        for i in range(0, self.N):
            linha = []
            for j in range(0, self.M):
                linha.append(-1)
            self.delta.append(linha)

    def conecta(self, v, expressaoRegular, u):
        padrao = re.compile(expressaoRegular)
        listaSimbolos = padrao.findall(self.alfabeto)
        for simbolo in listaSimbolos:
            self.delta[v][ord(simbolo)] = u

    def buildDelta(self):
        self.initDelta()
        for aresta in self.automato:
            v = aresta[0]
            expressaRegular = aresta[1]
            u = aresta[2]
            self.conecta(v, expressaRegular, u)


class AnalisadorLexico:
    def __init__(self):
        from automato_principal import alfabeto, estadosFinais, automato, num_estados
        self.dfa = Dfa(alfabeto, estadosFinais, automato, num_estados)
    def mySplit(self, arquivo):
        l = ['\n']
        for linha in arquivo:
            for simb in linha:
                l.append(simb)
        return l

    def get_comentario(self, l, indice, newDfa):
        topo = 1
        acu = ""
        while topo != 0:
            lexema = ""
            pilha = []
            estadoAtual = 0
            if indice == len(l):
                break
            while(indice < len(l)):
                simbolo = str(l[indice])         
                if newDfa.delta[estadoAtual][ord(simbolo)] == -1:
                    break
                lexema += simbolo
                pilha.append(estadoAtual)
                estadoAtual = newDfa.delta[estadoAtual][ord(simbolo)]
                indice+=1
         
            while not (estadoAtual in newDfa.estadosFinais) and pilha:
                estadoAtual = pilha.pop()
                lexema = lexema[0:len(lexema)-1]
                indice -= 1

            if not pilha:
                print("Erro")
                exit(0)

            acu += lexema
            if newDfa.estadosFinais[estadoAtual] == "ABERTURA":
                topo+=1
            else:
                topo-=1

        if topo != 0:
            print("Erro!")
            exit(0)
        
        return acu        

    def geraTokens(self, arquivo):
        listaTokens = []
        indice = 0
        l = self.mySplit(arquivo)
        pilha_indentacao = []
        pilha = []
        estadoAtual = 0
        while True:
            lexema = ""
            pilha = []
            estadoAtual = 0
            if indice == len(l):
                break
            while(indice < len(l)):
                simbolo = str(l[indice])            
                if self.dfa.delta[estadoAtual][ord(simbolo)] == -1:
                    break
                lexema += simbolo
                pilha.append(estadoAtual)
                estadoAtual = self.dfa.delta[estadoAtual][ord(simbolo)]
                indice+=1

            while not (estadoAtual in self.dfa.estadosFinais) and pilha:
                estadoAtual = pilha.pop()
                lexema = lexema[0:len(lexema)-1]
                indice -= 1
            #print(estadoAtual)
            #print ([l[x] for x in range(indice, len(l))])
            
            if not pilha:
                print("Erro")
                exit(0)
            
            if self.dfa.estadosFinais[estadoAtual] == "COMECO_COMENTARIO":
                from automato_comentario import alfabeto, estadosFinais, automato, num_estados
                newDfa = Dfa(alfabeto, estadosFinais, automato, num_estados)
                comentario = self.get_comentario(l, indice, newDfa)
                listaTokens.append( ("/*" + comentario, "COMENTARIO" ) )
                indice += len(comentario)
            
            elif self.dfa.estadosFinais[estadoAtual] == "INDENTACAO":
                tam = len(lexema) - 1
                if not pilha_indentacao:
                    if tam > 0:
                        print("Erro de indentação")
                        exit(0)
                    pilha_indentacao.append(tam)

                topo = len(pilha_indentacao) - 1
                if pilha_indentacao[topo] == tam:
                    continue
                if pilha_indentacao[topo] < tam:
                    pilha_indentacao.append(tam)
                    listaTokens.append(("begin", "BEGIN"))
                else:
                    while pilha_indentacao and pilha_indentacao[topo] != tam:
                        listaTokens.append(("end", "END"))
                        topo-=1
                        pilha_indentacao.pop()
                    if not pilha_indentacao:
                        print("Erro de indentação")
                        exit(0)
            else:
                listaTokens.append( (self.dfa.estadosFinais[estadoAtual], lexema) )
        while len(pilha_indentacao) > 1:
            listaTokens.append(("end", "END"))
            pilha_indentacao.pop()
        return listaTokens



def main():
    analisador = AnalisadorLexico()
    arq = open("./Testes/teste1.txt", "r")
    arquivo = arq.readlines()
    print(analisador.geraTokens(arquivo))

if __name__ == "__main__":
    main()
    

