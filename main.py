import random

tentativas = 5

palavras = ["loira", "manta", "fraco", "pouco", "trigo", "certo", "venho"]
palavra_escolhida = random.choice(palavras)

palpite = input("Digite seu palpite: ")
tentativa_atual = 1

while tentativa_atual < tentativas:
    letra_atual = 0
    for letra in palpite:
        if letra == palavra_escolhida[letra_atual]:
            print(f"\033[32m{letra.upper()}\033[0;0m", end=" ")
        else:
            if letra in palavra_escolhida:
                print(f"\033[33m{letra.upper()}\033[0;0m", end=" ")
            else:
                print(f"{letra.upper()}", end=" ")
        letra_atual += 1
    if palpite == palavra_escolhida:
        print("\nVocê acetou!")
        break
    tentativa_atual += 1
    palpite = input("\nDigite um novo palpite: ")
    if palpite == palavra_escolhida:
        print("\nVocê acetou!")
        break

if palpite != palavra_escolhida:
    print(f"VOCÊ ERROU! A PALAVRA ERA {palavra_escolhida.upper()}")