import re
from pylatexenc.latex2text import LatexNodes2Text


print('''Qual arquivo deverá ser analisado?
[] teste1
[] teste2
[] teste3
[] teste4

    Para utilizar um arquivo diferente, personalize previamente o arquivo teste4. No
    arquivo estão os comandos necessários para se escrever qualquer expressão lógica 
    em latex. Ao incluir novas expressões, certifique-se de utilizar os 
    comandos definidos !
 ''')
opcao = str(input('Nome do arquivo escolhido: '))

def barra_n(frase):
  # function to remove the \n character from the end of the line.
  # its use is necessary, because in some cases, the program reads
  # the \n at the end of the expressions, making it impossible to correctly process
  # the expressions.
  if frase.count('\n') != 0:
    return re.sub(r'\n', '', frase)

def operators():
  # function to return the grammatical operators
  operador_unario = '¬'
  operadores_binarios = ('∧', '↔', '∨', '→')
  abre_paren = '('
  fecha_paren = ')'
  const = ('T', 'F')

  return operador_unario, operadores_binarios, abre_paren, fecha_paren, const


def proposicao(char):
  # function to characterize and delimit propositions according to the grammar.
  lista = list(map(chr, range(97, 123)))
  lista_num = list(map(chr, range(48, 58)))

  return char in lista or char in lista_num


def formula_unaria(char):
  # function to determine whether the operator in the current iteration is unary.
  operador_unario, _, _, _, _ = operators()
  return char == operador_unario and char not in s1[-2]


def formula_binaria(char):
  # function to determine whether the operator in the current iteration is binary.
  _, operadores_binarios, _, _, _ = operators()
  return char in operadores_binarios and char not in s1[-2]


def iteracao(s1, state):
  # main function, responsible for iterating over the expressions.
  # its logic is based on the concept of Finite State Machines.
  operador_unario, operadores_binarios, abre_paren, fecha_paren, const = operators()
  contp = 0
  cont = None
  for i, char in enumerate(s1):
      if frase == "\n":
          exit()

      # first state
      if state == "CheckBrackets":

          if char == abre_paren:
              state = "CheckOperator"
              contp += 1
              continue
          elif char in const:
              return len(s1) == 1
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


def final_validation():
  if contp == 0 and iteracao(s1, state):
    if t > 3 and t1 and t2 == t and t3 == 0:
        print("Inválida")
    else:
        print("Válida")
  else:
    print("Inválida")


# open the txt file.
with open(opcao + ".txt", 'r') as arquivo:
  linha = int(arquivo.readline())

  while linha > 0:
      # initializes the processing of the expresions
      # calling the main function.
  
      # initial state
      state = "CheckBrackets"
  
      contp = 0
      frase = arquivo.readline()
  
      # using a python library to handle LaTeX.
      s = LatexNodes2Text().latex_to_text(barra_n(frase))
      s1 = re.findall(r'\S', s)
      operador_unario, operadores_binarios, abre_paren, fecha_paren, const = operators()
  
      # aditional checks.
      t = s1.count(operador_unario)
      t1 = s1.count(abre_paren)
      t2 = s1.count(fecha_paren)
      t3 = s1.count(operadores_binarios)
  
      # final validation to determine if the expression is valid.
      final_validation()
  
      linha -= 1