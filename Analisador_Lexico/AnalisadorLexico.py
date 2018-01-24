#Análise Lexica

alfabeto = ['$','(', ')', '+', '-','0', '1', '2', '3', '4', '5', '6', '7', '8', '9',';','<', '=', '>', 'A', 'B', 
	    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z', '[',']', '_','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z','{', '}','.']

estadosFinais = {1:"(", 2:"-", 3: "--", 4:"+", 5:"++", 6:"NUM", 7:"NUM", 8:"NUM", 10: "ID", 11: "ID", 21:"=", 20: ";", 16: "[",
                 17: "]", 14: "{", 15: "}", 13:")", 18: "CONST", 19: "CONST", 22: "ID", 23: "ID", 24: "for", 25: "ID", 26: "if",
                 27: "ID", 28: "ID", 29: "ID", 30: "ID", 31: "while", 32: "ID", 33: "ID", 36: "ID", 35: "ID", 34: "print", 37:"SPACE", 38: "=="}

delta = []

def initDelta():
    for i in range(0, 50):
        linha = []
        for j in range(0, 300):
            linha.append(-1)
        delta.append(linha)


def conecta(v, listaSimbolos, u):
    for simbolo in listaSimbolos:
        delta[v][ord(simbolo)] = u

def buildDelta():
    initDelta()
    conecta(0, [' ', '\n', '\t', '\r'], 37)
    conecta(21, '=', 38)
    conecta(0, ['='], 21)
    conecta(0, [';'], 20)
    conecta(0, ['['], 16)
    conecta(0, [']'], 17)
    conecta(0, ['{'], 14)
    conecta(0, ['}'], 15)
    conecta(0, ['('], 1)
    conecta(0, [')'], 13)
    conecta(0, ['-'], 2)
    conecta(2, ['-'], 3)
    conecta(0, ['+'], 4)
    conecta(4, ['+'], 5)
    conecta(0, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6)
    conecta(6, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6)
    conecta(6, ['.'], 7)
    conecta(7, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8)
    conecta(8, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8)
    conecta(0, ['.'], 9)
    conecta(9, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] , 8)
    conecta(0, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 18)
    conecta(18, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 19)
    conecta(19, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 19)
    conecta(0, ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'q',
                'r', 's', 't', 'u', 'v', 'x',  'y', 'z'], 10)
    conecta(10, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o','p','q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(11, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o','p','q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(0, ['&'], 12)
    conecta(12, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(0, ['f'], 22)
    conecta(22, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(22, ['o'], 23)
    conecta(23, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o','p', 'q', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(23, ['r'], 24)
    conecta(24, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(0, ['i'], 25)
    conecta(25, ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(25, ['f'], 26)
    conecta(26, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
                 ,'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(0, ['w'], 27)
    conecta(27, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(27, ['h'] , 28)
    conecta(28, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o','p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(28, ['i'], 29)
    conecta(29, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o','p','q',
                 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(29, ['l'], 30)
    conecta(30, ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p'
                 ,'q', 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(30, ['e'], 31)
    conecta(31, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(0, ['p'], 32)
    conecta(32, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o','p', 'q', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(32, ['r'], 33)
    conecta(33, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's'
                 , 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(33, ['i'], 36)
    conecta(36, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o','p', 'q', 'r', 's'
                 , 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(36, ['n'], 35)
    conecta(35, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's'
                 , 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)
    conecta(35,['t'], 34)
    conecta(34, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's'
                 , 't', 'u', 'v', 'w', 'x',  'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'], 11)

def classifica(lexema):
    estadoAtual = 0
    for simbolo in lexema:
        estadoAtual = delta[estadoAtual][ord(simbolo)]
        if estadoAtual == -1:
            break;
    if estadoAtual in estadosFinais:
        return (estadosFinais[estadoAtual], lexema)        
    return ("null", lexema)
    
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
        topo = len(pilha)-1
        while not (estadoAtual in estadosFinais) and topo > -1:
            estadoAtual = pilha[topo]
            lexema = lexema[0:len(lexema)-1]
            topo -= 1
            indice -= 1
        if topo == -1:
            print("Erro")
            exit(0)
        listaTokens.append( (estadosFinais[estadoAtual], lexema) )
    return listaTokens

buildDelta()
arquivo = open("teste.txt","r")
texto = arquivo.readlines()
print(geraTokens(texto))




