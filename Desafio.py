from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
jogador= int(input("O que deseja jogar?\n"
                   "0 -> Pedra\n"
                   "1 -> Papel\n"
                   "3 -> Tesoura"))

if computador == 0:
    if jogador == 0:
        print(f"O computador jogou Pedra e o jogador também! JOGO EMPATADO")
    elif jogador == 1:
        print(f"O computador jogou Pedra e o jogador Papel! JOGADOR VENCEU")
    elif jogador == 2:
        print(f"O computador jogou Pedra e o jogador Tesoura! COMPUTADOR VENCEU")

if computador == 1:
    if jogador == 0:
        print(f"O computador jogou Papel e o jogador também! COMPUTADOR VENCEU")
    elif jogador == 1:
        print(f"O computador jogou Papel e o jogador Papel!  JOGO EMPATADO")
    elif jogador == 2:
        print(f"O computador jogou Papel e o jogador Tesoura! JOGADOR VENCEU")

if computador == 2:
    if jogador == 0:
        print(f"O computador jogou Tesoura e o jogador também! JOGADOR VENCEU")
    elif jogador == 1:
        print(f"O computador jogou Tesoura e o jogador Papel! COMPUTADOR VENCEU")
    elif jogador == 2:
        print(f"O computador jogou Tesoura e o jogador também! JOGO EMPATADO")

