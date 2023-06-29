"""""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma 
prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número 
de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser
pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser 
pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim 
continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa 
deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de 
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos 
sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros
por dia de atraso.
"""



def valorPagamento (a, b):
    if b ==0:
        return a
    else:
        multa = a*0.03
        atraso = b*0.01
        total = a + multa + atraso
        return total

#a = int(input("Digite o valor da prestação"))
#b = int(input("Digite os dias em atrazo"))

valorRecebido =0
valorTotalPago=0

while True:
    a = float(input("Digite o valor da prestação"))    
    if a == 0:
        print("Programa finalizado com sucesso")
        print("Relatório:")
        print(f"Foram realizados {valorRecebido} pagamentos")
        print(f"e o valor recebido foi {valorTotalPago}")
        break
    b = int(input ("Quantos dias de atraso"))
    total = valorPagamento(a,b)
    valorRecebido +=1
    valorTotalPago +=total
    #valorRecebido.append(valorPagamento.total)