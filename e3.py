#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(n1, n2, n3):    
    aux = (n1) + (n2) + (n3)
    return aux

n1=int(input("Coloque o primeiro número"))
n2= int(input("Coloqie o segundo número"))
n3= int(input("Coloque o terceiro número"))

aux2 = soma(n1, n2, n3)

print(aux2)

