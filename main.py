import random
from functions import novo_palpite, verifica_letra, verifica_acerto

tentativas = 5

palavras = ["loira", "manta", "fraco", "pouco", "trigo", "certo", "venho"]
palavra_escolhida = random.choice(palavras)

palpite = input("Digite seu palpite: ")
tentativa_atual = 1

while tentativa_atual < tentativas:
    verifica_letra(palpite, palavra_escolhida)
    if verifica_acerto(palpite, palavra_escolhida):
        break
    palpite = novo_palpite()
    tentativa_atual += 1

if palpite != palavra_escolhida:
    print(f"VOCÊ ERROU! A PALAVRA ERA {palavra_escolhida.upper()}")