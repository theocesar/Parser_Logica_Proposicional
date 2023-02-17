'''
// Théo César Zanotto da Silva

Criar um algoritmo que seja capaz de validar expressões de lógica propisicional
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos, com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal e constituirá de uma linha de saída
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
# To initialize the program, a txt file name must be chosen and typed in the command line.

# open the txt file.
arquivo = open(opcao + ".txt", 'r')
linha = int(arquivo.readline())


def barran(frase):
    # function to remove the \n character from the end of the line.
    # its use is necessary, because in some cases, the program reads
    # the \n at the end of the expressions, making it impossible to correctly process
    # the grammatical analysis.
    if frase.count('\n') != 0:
        frase = re.sub(r'\n', '', frase)
    else:
        pass

    return frase


# grammatical symbols
operador_unario = '¬'
operadores_binarios = ('∧', '↔', '∨', '→')
abre_paren = '('
fecha_paren = ')'
const = ('T', 'F')


def proposicao(char):
    # function to characterize and delimit propositions according to the grammar.
    lista = list(map(chr, range(97, 123)))
    lista_num = list(map(chr, range(48, 58)))

    if char in lista:
        return True
    elif char in lista_num:
        return True
    else:
        return False


def formula_unaria(char):
    # function to determine whether the operator in the current iteration is unary.
    if char == operador_unario:
        if char in s1[-2]:
            return False
        else:
            return True


def formula_binaria(char):
    # function to determine whether the operator in the current iteration is binary.
    if char in operadores_binarios:
        if char in s1[-2]:
            return False
        else:
            return True


def iteracao(s1, state):
    # main function, responsible for iterating over the expressions.
    # its logic is based on the concept of Finite State Machines.
    contp = 0
    cont = None
    for i, char in enumerate(s1):
        if frase == "\n":
            exit()
            return True

        # first state
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

        # second state
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

        # third state
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

        # forth state
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

        # fifth state
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

        # sixth state
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

        # seventh state
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
    # initializes the processing of the expresions
    # calling the main function.

    # initial state
    state = "CheckBrackets"

    contp = 0
    frase = arquivo.readline()

    # using a python library to handle LaTeX.
    s = LatexNodes2Text().latex_to_text(barran(frase))
    # using regex
    s1 = re.findall(r'\S', s)

    # necessary checks.
    t = s1.count(operador_unario)
    t1 = s1.count(abre_paren)
    t2 = s1.count(fecha_paren)
    t3 = s1.count(operadores_binarios)

    # takes the final value of the main function and passes to the terminal whether the expression
    # is valid or not.
    if contp == 0 and iteracao(s1, state):
        if t > 3:
            if t1 and t2 == t and t3 == 0:
                print("Inválida")
        else:
            print("Válida")
    else:
        print("Inválida")

    linha -= 1
