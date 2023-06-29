"""""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres
 ‘ + ’ , ‘ − ’ e ‘ | ‘. Esta função deve receber dois parâmetros, 
 linhas e colunas, sendo que o valor por omissão é o valor mínimo igual
   a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
   eles devem ser modificados para valores dentro da faixa de forma elegante.
"""
def moldura (linhas, colunas, quina, espaco):
    linhas = "-"
    colunas = "|"
    quina = "+"
    espaco = " "
    return linhas, colunas, quina, espaco


i = int(input("Qual largura do retangulo?"))
k = int (input("Qual a altura do retangulo?"))

o = moldura(i, k, 4, i)

print(f"{o[2]} {o[0]*i} {o[2]}")
for j in range (k):   
    print((f"{o[1]} {(o[3])*i} {o[1]}"))

print(f"{o[2]} {(o[0])*i} {o[2]}")
