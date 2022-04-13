import random
from functions import novo_palpite, verifica_letra, verifica_acerto

palavras = []
tentativas = 5

arquivo = open("palavras.txt", "r")
for linha in arquivo:
    palavras.append(linha)

palavra_escolhida = random.choice(palavras)
palavra_escolhida = palavra_escolhida[:len(palavra_escolhida)-1]

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

arquivo.close()