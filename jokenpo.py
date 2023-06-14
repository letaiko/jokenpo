# imprime o menu
print("\n♡♡♡ | Jokenpô | ♡♡♡ \n1 - humano x humano \n2 - humano x computador \n3 - computador x computador \n")

# escolha da modalidade
modalidade = int(input("Escolha a modalidade: "))

# em caso de uma modalidade inválida
while modalidade != 1 and modalidade != 2 and modalidade != 3:
    modalidade = int(input("\nModalidade inválida! Escolha entre 1, 2 ou 3: "))

# modalidade 1 - humano x humano
if modalidade == 1:
    # nomes dos jogadores humano x humano
    nome1 = input("\nDigite o nome do primeiro jogador: ")
    nome2 = input("Digite o nome do segundo jogador: ")
    print("\nOlá " + nome1 + " e " + nome2 + "! Vamos começar a jogar!\n")

    # recolhe as jogadas
    print("Escolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
    jogador1 = int(input("A escolha de " + nome1 + " é: "))
    jogador2 = int(input("A escolha de " + nome2 + " é: "))
    sair = 0 or 1
    pontos1 = 0
    pontos2 = 0

    # enquanto quiserem continuar a jogar
    while sair != 0:
        # em caso de empate
        if (jogador1 == 1 and jogador2 == 1) or (jogador1 == 2 and jogador2 == 2) or (jogador1 == 3 and jogador2 == 3):
            print(
                "\nVocês empataram!" + "\n\n" + nome1 + " x " + nome2 + "\n" + str(pontos1) + " x " + str(pontos2))
        # jogadas em que o jogador 2 ganha
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (
                jogador1 == 3 and jogador2 == 1):
            pontos2 += 1  # atualiza pontos e placar
            print("\n" + nome2 + " ganhou!" + "\n\n" + nome1 + " x " + nome2 + "\n" + str(pontos1) + " x " + str(
                pontos2))
        # jogadas em que o jogador 1 ganha
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (
                jogador1 == 3 and jogador2 == 2):
            pontos1 += 1  # atualiza pontos e placar
            print("\n" + nome1 + " ganhou!" + "\n\n" + nome1 + " x " + nome2 + "\n" + str(pontos1) + " x " + str(
                pontos2))
        # no caso de jogadas inválidas
        else:
            print("\nJogada inválida, tente novamente!")

        # mensagem de continuar ou sair
        print("\nVocê quer continuar o jogo?")
        sair = int(input("Se quiser continuar, digite qualquer número. Caso queira sair, digite 0: "))

        # caso a escolha seja sair, imprime mensagem e placar
        if sair == 0:
            print("\n\n\n♡♡♡ Andressa, Anna, Letícia, Michele e Yejin agradecem por jogar nosso jokenpô! ♡♡♡ \n\n\n♡♡♡ | Placar | ♡♡♡ \n" + nome1 + " x " + nome2 + "\n" + str(pontos1) + " x " + str(pontos2))
        # continuar o jogo, recolher as próximas jogadas
        else:
            print("\nEscolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
            jogador1 = int(input("A escolha de " + nome1 + " é: "))
            jogador2 = int(input("A escolha de " + nome2 + " é: "))


# modalidade 2 - humano x computador
elif modalidade == 2:
    nome = input("\nDigite o seu nome aqui: ")
    print("\nOlá, " + nome + "! Vamos começar jogar!\n")

    # jogada do computador é randômica
    import random

    opcao = [1, 2, 3]  # possíveis jogadas do computador
    jogador2 = random.choice(opcao)
    sair = 0 or 1
    pontos1 = 0
    pontos2 = 0
    # jogada da pessoa
    print("Escolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
    jogador1 = int(input("A sua escolha é: "))

    # enquanto quiserem continuar a jogar
    while sair != 0:
        # em caso de empate
        if jogador1 == jogador2:
            print("O computador jogou " + str(jogador2) + "\nVocês empataram!" + "\n\n" + nome + " x computador" + "\n" + str(pontos1) + " x " + str(pontos2))
        # jogadas em que o jogador 1 ganha
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (
                jogador1 == 3 and jogador2 == 2):
            pontos1 += 1  # atualiza pontos e placar
            print("O computador jogou " + str(jogador2) + "\n" + nome + " ganhou!" + "\n\n" + nome + " x computador" + "\n" + str(pontos1) + " x " + str(pontos2))
        # jogadas em que o computador ganha
        elif (jogador1 == 2 and jogador2 == 3) or (jogador1 == 1 and jogador2 == 2) or (
                jogador1 == 3 and jogador2 == 1):
            pontos2 += 1  # atualiza pontos e placar
            print("O computador jogou " + str(jogador2) + "\n" + "O computador ganhou!" + "\n\n" + nome + " x computador" + "\n" + str(pontos1) + " x " + str(pontos2))
        # no caso de jogadas inválidas
        else:
            print("\nJogada inválida, tente novamente!")

        # mensagem de continuar ou sair
        print("\nVocê quer continuar o jogo?")
        sair = int(input("Se quiser continuar, digite qualquer número. Caso queira sair, digite 0: "))

        # caso a escolha seja sair, imprime mensagem e placar
        if sair == 0:
            print("\n\n\n♡♡♡ Andressa, Anna, Letícia, Michele e Yejin agradecem por jogar nosso jokenpô! ♡♡♡ \n\n\n♡♡♡ | Placar | ♡♡♡ \n" + nome + " x computador" + "\n" + str(pontos1) + " x " + str(pontos2))
        # continuar o jogo, recolher as próximas jogadas
        else:
            print("\nEscolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
            jogador1 = int(input("A sua escolha é: "))
            jogador2 = random.choice(opcao)

# modalidade 3 - computador x computador
elif modalidade == 3:
    import random

    # jogadas dos computadores são randômicas
    select = [1, 2, 3] # possíveis jogadas
    jogador1 = random.choice(select)
    jogador2 = random.choice(select)
    sair = 0 or 1
    pontos1 = 0
    pontos2 = 0
    print("\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")

    # enquanto quiserem continuar a jogar
    while sair != 0:
        # em caso de empate
        if jogador1 == jogador2:
            print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(
                jogador2) + "\nEmpate!" + "\n\ncomputador 1 x computador 2" + "\n" + str(pontos1) + " x " + str(
                pontos2))
        # jogadas em que o computador 1 ganha
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (
                jogador1 == 3 and jogador2 == 2):
            pontos1 += 1  # atualiza pontos e placar
            print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(
                jogador2) + "\nO computador 1 ganhou!" + "\n\ncomputador 1 x computador 2" + "\n" + str(
                pontos1) + " x " + str(pontos2))
        # jogadas em que o computador 2 ganha
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (
                jogador1 == 3 and jogador2 == 1):
            pontos2 += 1  # atualiza pontos e placar
            print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(
                jogador2) + "\nO computador 2 ganhou!" + "\n\ncomputador 1 x computador 2" + "\n" + str(
                pontos1) + " x " + str(pontos2))

        # mensagem de continuar ou sair
        print("\nVocê quer continuar o jogo?")
        sair = int(input("Se quiser continuar, digite qualquer número. Caso queira sair, digite 0: "))

        # caso a escolha seja sair, imprime mensagem e placar
        if sair == 0:
            print("\n\n\n♡♡♡ Andressa, Anna, Letícia, Michele e Yejin agradecem por jogar nosso jokenpô! ♡♡♡ \n\n\n♡♡♡ | Placar | ♡♡♡\n" + "computador 1 x computador 2" + "\n" + str(
                    pontos1) + " x " + str(pontos2))
        # continuar o jogo, recolher as próximas jogadas
        else:
            print("\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
            jogador1 = random.choice(select)
            jogador2 = random.choice(select)
