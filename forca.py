import funcoes
import random

def tratar_letra(letra):
    tratar = letra.lower()
    tratar = tratar.strip()
    return tratar


def jogar_forca():
    funcoes.estrelinha_frase_forca_intro("   Bem-Vindo ao jogo da forca!")

    arquivo = open("palavra.txt", "r")
    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)

    arquivo.close()
    contador = random.randrange(0,len(lista_palavras))
    palavra_secreta = lista_palavras[contador]

    salvar = []
    letra_acertadas = ["_" for contador in palavra_secreta]
    acertou = False
    enforcou = False
    chute = None
    tentativa = 5
    funcoes.estrelinha_frase_forca(" ".join(letra_acertadas))

    while(not enforcou and not acertou):

        if(chute == None):
            chute = input("Digite seu chute: ")
            chute = tratar_letra(chute)
        else:
            chute = input("Digite novamente seu chute: ")
            chute = tratar_letra(chute)

        if(chute in palavra_secreta):
            if (chute in salvar):
                print("Você já digitou esta letra. Tente outra!")
                continue
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letra_acertadas[posicao] = chute.upper()
                posicao += 1
        else:
            if (chute in salvar):
                print("Você já digitou esta letra. Tente outra!")
                continue
            tentativa -= 1
            match tentativa:
                case 4:
                    funcoes.desenhar_forca_um()
                    print(f"Não tem a letra {chute.upper()}. Você tem {tentativa} chances.")
                case 3:
                    funcoes.desenhar_forca_dois()
                    print(f"Não tem a letra {chute.upper()}. Você tem {tentativa} chances.")
                case 2:
                    funcoes.desenhar_forca_tres()
                    print(f"Não tem a letra {chute.upper()}. Você tem {tentativa} chances.")
                case 1:
                    funcoes.desenhar_forca_quatro()
                    print(f"Não tem a letra {chute.upper()}. Você tem {tentativa} chances.")
                case _:
                    funcoes.desenhar_forca_cinco()
                    print(f"Não tem a letra {chute.upper()}. Você perdeu!")

        salvar.append(chute)
        enforcou = tentativa <= 0
        acertou = "_" not in letra_acertadas

        print("")
        if(tentativa > 0):
            funcoes.estrelinha_frase_forca_dois(" ".join(letra_acertadas))

    if(enforcou):
        print(f"\nVocê enforcou! :'( A palavra era {palavra_secreta.upper()}.")
    else:
        print("\nVocê Ganhou! :D")


if(__name__ == "__main__"):
    jogar_forca()