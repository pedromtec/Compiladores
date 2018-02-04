#Análise Lexica
import re

alfabeto = "&()+-0123456789;=ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_abcdefghijklmnopqrstuvwxyz{}.\n\t \r"

estadosFinais = {1:"(", 2:"-", 3: "--", 4:"+", 5:"++", 6:"NUM", 7:"NUM", 8:"NUM", 10: "ID", 11: "ID", 21:"=", 20: ";", 16: "[",
                 17: "]", 14: "{", 15: "}", 13:")", 18: "CONST", 19: "CONST", 22: "ID", 23: "ID", 24: "for", 25: "ID", 26: "if",
                 27: "ID", 28: "ID", 29: "ID", 30: "ID", 31: "while", 32: "ID", 33: "ID", 36: "ID", 35: "ID", 34: "print", 37:"SPACE", 38: "=="}
grafo = [
          (0, "[' ''\n''\t''\r']", 37), (21,"[=]", 38), (0, "[=]", 21), (0, "[;]", 20), (0, "[[]", 16), (0, "[]]", 17), (0, "[{]", 14),
          (0, "[}]", 15), (0, "[(]", 1), (0, "[)]", 13), (0, "[-]", 2), (2, "[-]", 3), (0, "[+]", 4), (4, "[+]", 5), (0, "[0-9]", 6),
          (6, "[0-9]" , 6), (6, "[.]", 7), (7,"[0-9]", 8), (8, "[0-9]", 8), (0, "[.]", 9), (9, "[0-9]" , 8), (0, "[A-Z]", 18),
          (18, "[A-Z0-9_]", 19), (19, "[A-Z0-9_]", 19), (0, "[a-eg-hj-oq-vx-z]", 10), (10, "[a-z0-9_]", 11), (11, "[a-z0-9_]", 11),
          (0, "[&]", 12), (12, "[a-z0-9_]", 11), (0, "[f]", 22), (22, "[a-qs-z0-9_]", 11),  (22, "[o]", 23), (23, "[a-qs-z0-9_]", 11),
          (23, "[r]", 24), (24, "[a-z0-9_]", 11), (0, "[i]", 25), (25, "[a-eg-z0-9_]", 11), (25, "[f]", 26), (26, "[a-z0-9_]", 11),
          (0, "[w]", 27), (27, "[a-gi-z0-9_]", 11),  (27, "[h]", 28), (28,"[a-hj-z0-9_]" ,11), (28, "[i]", 29), (29, "[a-jk-z0-9_]", 11),
          (29, "[l]", 30), (30, "[a-df-z0-9_]", 11), (30, "[e]", 31), (31, "[a-z0-9_]", 11), (0, "[p]", 32), (32, "[a-qs-z0-9_]", 11),
          (32, "[r]", 33), (33, "[a-hj-z0-9_]", 11), (33, "[i]", 36), (36,"[a-mo-z0-9_]",11), (36, "[n]", 35), (35, "[a-su-z0-9_]", 11),
          (35, "[t]", 34), (34, "[a-z0-9_]", 11)
        ]


delta = []
N = 50
M = 300

def initDelta():
    for i in range(0, N):
        linha = []
        for j in range(0, M):
            linha.append(-1)
        delta.append(linha)

def conecta(v, expressaoRegular, u):
    padrao = re.compile(expressaoRegular)
    listaSimbolos = padrao.findall(alfabeto)
    for simbolo in listaSimbolos:
        delta[v][ord(simbolo)] = u

def buildDelta():
    initDelta()
    for aresta in grafo:
        v = aresta[0]
        expressaRegular = aresta[1]
        u = aresta[2]
        conecta(v, expressaRegular, u)
        
def mySplit(arquivo):
    l = []
    for linha in arquivo:
        for simb in linha:
            l.append(simb)
    return l

def geraTokens(arquivo):
    listaTokens = []
    indice = 0
    l = mySplit(arquivo)
    while True:
        lexema = ""
        pilha = []
        estadoAtual = 0
        if indice == len(l):
            break
        while(indice < len(l)):
            simbolo = str(l[indice])            
            if delta[estadoAtual][ord(simbolo)] == -1:
                break
            lexema += simbolo
            pilha.append(estadoAtual)
            estadoAtual = delta[estadoAtual][ord(simbolo)]
            indice+=1  
        while not (estadoAtual in estadosFinais) and pilha:
            estadoAtual = pilha.pop()
            lexema = lexema[0:len(lexema)-1]
            indice -= 1
        if not pilha:
            print("Erro")
            exit(0)
        listaTokens.append( (estadosFinais[estadoAtual], lexema) )
    return listaTokens


def main():
    buildDelta()
    arq = open("./Testes/teste1.txt", "r")
    arquivo = arq.readlines()
    print(geraTokens(arquivo))

if __name__ == "__main__":
    main()
    

