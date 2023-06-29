#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    1   2   3   ...  n para um n informado pelo usuário. 
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

#aqui pede a quantidade de vezes do usuário
k = int(input("Informe quantas vezes quer repetir a seguência, n"))

#   Funcao que inicia com uma string vazia, entra num "for" para calcular quantas vezes vai se repetir a seguencia 
#que vai ser incrementado a cada interação. Veja o número a ser escrito como uma string e não como um número!!!!
def make_string(k):
    s=" "
    for i in range(k):
        s+="{} ". format(i+1)
    return s

#for que irá printar a quantidade de vezes do usuário e incrementar +1 a cada iteração. 
for j in range(0,k):
    print(make_string(j+1))