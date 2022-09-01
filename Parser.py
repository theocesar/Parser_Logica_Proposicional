'''
// Théo César Zanotto da Silva

ENUNCIADO

Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.


Gramática:
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
Constante="T"|"F".
Proposicao=[a−z0−9]+
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
AbreParen="("
FechaParen=")"
OperatorUnario="¬"
OperatorBinario="∨"|"∧"|"→"|"↔"


Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação,
conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
qualquer expressão de entrada.
Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo
números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra
para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
programa carregando o arquivo de testes.
'''

from pylatexenc.latex2text import LatexNodes2Text

import re

print('''Qual arquivo deverá ser analisado?
[] teste1
[] teste2
[] teste3
[] teste4

    Para utilizar um arquivo diferente, personalize previamente o arquivo teste4. No
    arquivo estão os comandos necessários para se escrever qualquer expressão lógica em latex. Ao incluir novas expressões,
    certifique-se de utilizar os comandos definidos !
 ''')
opcao = str(input('Nome do arquivo escolhido: '))

# abre o arquivo txt.
arquivo = open(opcao + ".txt", 'r')
linha = int(arquivo.readline())


def barran(frase):
    # função para retirar o \n do final da última linha.
    # é necessária sua utilização, pois em alguns casos, o programa lê
    # o \n ao final das expressões, impossiblitando o processamento
    # correto da análise gramatical.
    if frase.count('\n') != 0:
        frase = re.sub(r'\n', '', frase)
    else:
        pass

    return frase

# todos os símbolos importantes para o processamento.
operador_unario = '¬'
operadores_binarios = ('∧', '↔', '∨', '→')
abre_paren = '('
fecha_paren = ')'
const = ('T', 'F')


def proposicao(char):
    # função para caracterizar e delimitar as proposições de acordo com a gramática.
    lista = list(map(chr, range(97, 123)))
    lista_num = list(map(chr, range(48, 58)))

    if char in lista:
        return True
    elif char in lista_num:
        return True
    else:
        return False


def formula_unaria(char):
    # função para determinar se o operador que está na iteração atual é unario.
    if char == operador_unario:
        if char in s1[-2]:
            return False
        else:
            return True


def formula_binaria(char):
    # função para determinar se o operador que está na iteração atual é binario.
    if char in operadores_binarios:
        if char in s1[-2]:
            return False
        else:
            return True


def iteracao(s1, state):
    # função primordial, na qual a expressão é processada.
    contp = 0
    cont = None
    for i, char in enumerate(s1):
        if frase == "\n":
            exit()
            return True
        if state == "CheckBrackets":

            if char == abre_paren:
                state = "CheckOperator"
                contp += 1
                continue
            elif char in const:
                if len(s1) == 1:
                    return True
                else:
                    return False
            else:
                return False

        if state == "CheckOperator":

            if formula_unaria(char):
                state = "Unario"
                cont = True
                continue
            elif formula_binaria(char):
                state = "Binario"
                cont = False
                continue
            else:
                return False

        if state == "Unario":

            if char == abre_paren:
                state = "CheckOperator"
                contp += 1
                continue

            if proposicao(char):
                state = "P1"
                continue

            if char == fecha_paren:
                state = "CheckClosing"
                contp -= 1
                continue

            if char in const:
                state = "CheckClosing"
                continue

            else:
                return False

        if state == "Binario":

            if char == abre_paren:
                state = "CheckOperator"
                contp += 1
                continue

            if proposicao(char):
                state = "P1"
                continue

            if char == fecha_paren:
                state = "CheckClosing"
                contp -= 1
                continue

            if char in const:
                state = "Binario"
                continue

        if state == "P1":

            if char != fecha_paren:

                if char not in list(map(chr, range(48, 58))):

                    if char in list(map(chr, range(97, 123))):
                        if cont is True and s[i].isspace() is True:
                            return False
                        continue
                    else:
                        return False
                else:
                    state = "P2"

            else:
                state = "CheckClosing"

        if state == "P2":

            if char != fecha_paren:

                if char not in list(map(chr, range(97, 123))):
                    if list(map(chr, range(48, 58))):
                        continue
                    else:
                        return False
                else:
                    state = "P1"

            else:
                state = "CheckClosing"

        if state == "CheckClosing":

            if char == abre_paren:
                state = "CheckOperator"
                contp += 1
                continue

            elif char == fecha_paren:
                state = "CheckClosing"
                cont = None
                contp -= 1
                if char in s1[-1]:
                    if contp == 0:
                        return True
                else:
                    continue

            elif proposicao(char):
                state = "P1"

            else:
                return False




while linha > 0:
    # inicializa o processamento das expressões e faz a conexão com a função principal.
    # recebe o valor final da função principal e passa para o terminal se a expressão
    # é válida ou não
    state = "CheckBrackets"
    contp = 0
    frase = arquivo.readline()
    s = LatexNodes2Text().latex_to_text(barran(frase))
    s1 = re.findall(r'\S', s)
    t = s1.count(operador_unario)
    t1 = s1.count(abre_paren)
    t2 = s1.count(fecha_paren)
    t3 = s1.count(operadores_binarios)
    if contp == 0 and iteracao(s1, state):
        if t > 3:
            if t1 and t2 == t and t3 == 0:
                print("Inválida")
        else:
            print("Válida")
    else:
        print("Inválida")

    linha -= 1
