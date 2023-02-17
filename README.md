# Parser_Logica_Proposicional
 
Algorithm that implements a parser to validate propositional logic expressions

## In depth explanation:

Create an algorithm that is able to validate propositional logic expressions
written in LaTeX and define whether they are grammatically correct expressions. You will validate only the form
of the expression (syntax).

The input will be provided by a text file, with the following formatting:

1. In the first line of this file there is an integer that tells you how many logical
logical expressions are in the file.

2. Each of the following lines contains a logical expression that must be validated.
The output of your program will be on the terminal and will consist of one line of output
for each input logical expression containing either the valid word or the invalid word and nothing else.


#### Grammar: <br />  

Formula=Constant|Proposition|FormulaUnaria|FormulaBinaria. <br /> 
Constant="T"|"F". <br /> 
Proposition=[a-z0-9]+ <br /> 
FormulaUnaria=AbreParen OperatorUnary Formula ClosesParen <br /> 
FormulaBinaria=AbreParen OperatorBinary Formula Formula CloseParen <br /> 
OpenParen="(" <br /> 
CloseParen=")" <br /> 
OperatorUnario="¬" <br /> 
OperatorBinario="∨"|"∧"|"→"|"↔" <br /> 


Each evaluated logical expression can have any combination of the negation operations,
conjunction, disjunction, implication, and bi-implication with no limits on the combining of prepositions and operations.

The logical values True and False are represented in the grammar and, as such, can be used in any input expression.
