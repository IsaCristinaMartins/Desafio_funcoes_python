# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def criatividade(n1):
    if n1 == "P":
        n1="Positivo"
    elif n1== "N" or n1=="0":
        n1="Negativo"
    return n1

n1 = str(input("Coloque P - Positivo ou N ou 0-Negativo"))

aux = criatividade(n1)

print(aux)

