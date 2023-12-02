from random import randint
intens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0,2)
print('''SUAS OPÇÔES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada"))
print("-=" * 14)
print("o computador escolheu {}" .format(intens[computador]))
print("o jogador escolheu {}" .format(intens[jogador]))
print("-=" * 14)
if computador == 0:
    if jogador == 0:
      print('EMPATE')
    elif jogador == 1:
      print('JOGADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('JOGDOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
