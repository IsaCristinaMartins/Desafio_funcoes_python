"""""
Data com mês por extenso. Construa uma função que receba uma data no formato 
DD/MM/AAAA e  devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

mesExtenso = ["", "Janeiro", \
                  "Fevereiro", \
                  "Março", \
                  "Abril",\
                  "Maio", \
                  "Junho", \
                  "Julho", \
                  "Agosto", \
                  "Setembro", \
                  "Novembro", \
                  "Dezembro"]



def teste ():
    data = str(input("Digite a data nesse formato: DD/MM/AAAA"))
    c = data.split("/")
    dia = int (c[0])
    ano = int (c[2])
    mes = int (c[1])
    return c, mes, dia, ano

b= teste()

if {b[2]} >=32:
    print("Data inválida")
    exit
else:
    print(f"A data por extenso é {b[2]}/ {mesExtenso[b[1]]}/ {b[3]}")
