import re
alfabeto = "&()+-0123456789;=ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_abcdefghijklmnopqrstuvwxyz{}.\n\t \r/*"
automato = [(0,"[^*^/]",0 ), (0, "[/]", 1), (1, "[/]", 1), (1,"[^*^/]",0), (1,"[*]", 2),
            (0,"[*]",3), (3,"[^*^/]",0), (3 ,"[*]", 3), (3, "[/]",4)]
estadosFinais = {2:"ABERTURA", 4:"FECHAMENTO"}
num_estados = 5


'''
padrao = re.compile("[^/^*]")
listaSimbolos = padrao.findall(alfabeto)

print(listaSimbolos)


def initDelta():
    for i in range(0, self.N):
        linha = []
        for j in range(0, self.M):
            linha.append(-1)
        self.delta.append(linha)
'''