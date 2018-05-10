import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)

    print("Escolha o nível de dificuldade  - (1) Fácil (2) Médio (3) Difícil")
    nivel = ""
    while not nivel.isdigit():
        nivel = input("Defina o nível: ")
    nivel = int(nivel)
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5
    else:
        print("Nivel selecionado incorreto, selecionando automaticamente o nivel difícil")
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Rodada: {} de {}".format(rodada, total_tentativas))

        chute = ""
        while not chute.isdigit():
            chute = input("Digite o seu palpite entre 1 e 100: ")
        chute = int(chute)

        while chute < 1 or chute > 100:
            print("O numero deve ser entre 1 e 100!")
            chute = ""
            while not chute.isdigit():
                chute = input("Digite o seu palpite entre 1 e 100: ")
            chute = int(chute)

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto

        print("Seu palpite foi: ", chute)

        if acertou:
            print("Parabéns, você acertou com {} tentativa(s)!".format(rodada))
            break
        else:
            if chute_maior:
                print("Você errou! Seu chute foi maior do que o número secreto!")
            else:
                print("Você errou! Seu chute foi menor do que o número secreto!")

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
