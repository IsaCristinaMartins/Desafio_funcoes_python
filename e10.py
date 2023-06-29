""""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
 Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
  Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
  Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
  Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
  Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
  """
import random

contador=0


def jogada():
   dado1 = random.randint(1,6)
   dados2 = random.randint(1,6)
   return dado1 + dados2

lancamento1= jogada()

if lancamento1 == 7 and lancamento1 ==11:
    print(f"Você é um natural e ganhou. Seu número da sorte foi {lancamento1}")
    exit
elif lancamento1 == 2 and lancamento1 == 3 and lancamento1 ==12:
    print (f"CRAPS -  Você perdeu!. Você tirou o número proibido {lancamento1}")
    exit
elif lancamento1 >=4 and lancamento1 <=10:
    contador+=1
    while True:
        segundo_lancamento = jogada()
        if segundo_lancamento == lancamento1:
            print(f"Voce ganhou, parabéns. Suas jogadas foram {lancamento1} e {segundo_lancamento}. Você marcou {contador} ponto!")
            break
        elif segundo_lancamento ==7:
            print (f"CRAPS -  Você perdeu! Você tirou o número proibido {segundo_lancamento}, seus pontos foram {contador}")
            break
        else:
            contador+=1
            continue
             