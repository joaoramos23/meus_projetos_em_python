# JOGO DA FORCA CONSISTE EM VOCÊ TENTAR ADIVINHAR UMA PALAVRA #
# NESSE JOGO A 7 TENTATIVAS PARA TENTAR ACERTAS A PALAVRA #
# by: João Ramos #
import random


def jogo_forca():
    desenhar_nome_do_jogo()
    palavra_secreta = escolher_palavra_secreta()
    letras_acertadas = ["_" for contador in palavra_secreta]
    logica_jogo(letras_acertadas,palavra_secreta)

def tratar_entrada(chute):
    tratar = chute.lower()
    tratar = tratar.strip()
    return tratar

def logica_jogo(letras_acertadas,palavra_secreta):

    acertou = False
    enforcou = False
    tentativa = 7
    salvar = []
    print(" ".join(letras_acertadas))
    while (not acertou and not enforcou):
        chute = input("Digite uma letra: ")
        chute = tratar_entrada(chute)
        if(chute == "" or chute.isnumeric() or not chute.isalnum()):
            print("Porfavor digite uma letra!\n")
            continue
        if (len(chute) > 1):
            print("Porfavor digite apenas um caracter!\n")
            continue
        posicao = 0
        if (chute in palavra_secreta):
            if(chute in salvar):
                print(f"Você já digitou a letra {chute.upper()}, tente outra letra!\n")
                print(" ".join(letras_acertadas))
                continue
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = chute.upper()
                posicao += 1
            print("")
            print(" ".join(letras_acertadas))
        else:
            if (chute in salvar):
                print(f"Você já digitou a letra {chute.upper()}, tente outra letra!\n")
                print(" ".join(letras_acertadas))
                continue
            print(f"Não existe a letra {chute} na palavra.")
            tentativa -= 1
            desenhar_forca(tentativa)
            print(" ".join(letras_acertadas))
        salvar.append(chute)
        enforcou = tentativa <= 0
        acertou = "_" not in letras_acertadas
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenhar_forca(tentativa):
        print("  _______     ")
        print(" |/      |    ")

        if (tentativa == 6):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 5):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 4):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (tentativa == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (tentativa == 0):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta.upper()}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def escolher_palavra_secreta():
    lista_palavras = ["maça", "abacate", "melancia", "abacaxi", "laranja"]
    contador = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[contador]
    return palavra_secreta

def desenhar_nome_do_jogo():
    print("╔=====================================╗")
    print("║            JOGO DA FORCA            ║")
    print("╚=====================================╝")

if (__name__ == "__main__"):
    jogo_forca()
