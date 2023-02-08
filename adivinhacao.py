import random
import funcoes

def jogar_adivinhacao():

    funcoes.estrelinha_frase("Bem vindo ao jogo de adivinhação!")
    print("****    ESCOLHA SEU NIVEL    ****")
    print("****   1 - FACIL (1 a 50)    ****")
    print("****   2 - MEDIO (1 a 100)   ****")
    print("****   3 - DIFICIL (1 a 500) ****")
    print("*********************************")

    nivel_selecionado = None
    seleciona_nivel = False

    while(not seleciona_nivel):

        nivel = int(input("Escolha seu nivel: "))

        match nivel:
            case 1:
                nivel_selecionado = 51
                print("\nNivel: Facil.\n")
                seleciona_nivel = True
            case 2:
                nivel_selecionado = 101
                print("\nNivel: Medio.\n")
                seleciona_nivel = True
            case 3:
                nivel_selecionado = 301
                print("\nNivel: Dificil.\n")
                seleciona_nivel = True
            case _:
                print("Erro! Escolha o nível novamente")
                continue



    numero_secreto = random.randrange(1,nivel_selecionado)
    #random gera um número entre 0.0 e 1.0
    #random.seed(100) sempre vai gerar o numero da seed, no caso 19. Pseudo-Random.
    acertou = False
    tentativa = 1
    pontos = 1000

    print(f"Você esta na {tentativa}ª tentativa. Sua pontuação é: {pontos}")


    while(acertou == False):

        chute = int(input(f"Digite um número entre 1 e {nivel_selecionado -1}: "))

        if(chute < 1 or chute > nivel_selecionado -1):
            print("\nVocê digitou: {}.".format(chute))
            print(f"Você deve digitar um número entre 1 e {nivel_selecionado -1}. \nVocê perdeu 100 pontos!\n")
            tentativa = tentativa + 1
            pontos = pontos - 100
            if (pontos <= 0):
                print("Seus pontos acabaram você perdeu!")
                break

            print(f"Você esta na {tentativa}ª tentativa. Sua pontuação é: {pontos}")
            continue

        acertou = numero_secreto == chute
        baixo = numero_secreto > chute

        print(f"Você digitou: {chute}.\n")

        if (acertou):
            print("\n")
            funcoes.estrelinha_frase(f"Você acertou na {tentativa}ª tentativa! \nSua pontuação é: {pontos}.")
            break
        elif(baixo):
            print("Você errou! Você chutou para baixo! Tente um número maior! \nVocê perdeu 100 pontos!", end="\n\n")
            pontos = pontos - 100
            if(pontos <= 0):
                print("Seus pontos acabaram você perdeu!")
                break
        else:
            print("Você errou! Você chutou para cima! Tente um número menor! \nVocê perdeu 100 pontos!", end="\n\n")
            pontos = pontos - 100
            if (pontos <= 0):
                print("Seus pontos acabaram você perdeu!")
                break

        tentativa = tentativa + 1
        if(acertou == False):
            print(f"Você esta na {tentativa}ª tentativa. Sua pontuação é: {pontos}")

if(__name__ == "__main__"):
    jogar_adivinhacao()