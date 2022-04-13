def verifica_letra(palpite, palavra_escolhida):
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

def verifica_acerto(palpite, palavra_escolhida):
    if palpite == palavra_escolhida:
        print("\nVocê acertou!")
        return True
    else:
        return False

def novo_palpite():
    return input("\nDigite um novo palpite: ")