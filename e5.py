# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. A função “altera” o valor de
# custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto) * custo


imposto= float(input("Valor do imposto"))
vendas = int(input("Valor da venda"))

print(f"{somaImposto(imposto, vendas)}")