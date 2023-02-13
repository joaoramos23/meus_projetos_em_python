# JOGO DE ADIVINAÇÃO CONSISTEM EM VOCÊ TENTAR ADIVINHAR UM NÚMERO ALEATORIO #
# ESSE JOGO TEM 3 NIVEIS. CADA UM COM UMA QUANTIDADE DE TENTATIVAS E PERCA DE PONTOS #
# by: João Ramos #
import random

def jogo_adivinha_numero():
    desenhar_nome_do_jogo()
    qntd_numeros = selecionar_nivel()
    numero_secreto = random.randrange(0,qntd_numeros)
    logica_jogo_adivinha(qntd_numeros, numero_secreto)

def logica_jogo_adivinha(qntd_numeros,numero_secreto):
    ganhou = False
    perdeu = False
    salvar = []
    tentativa = 0
    tentativa_mostrar = 0
    pontuacao = 1000
    parametro_pontuacao = 0

    print(f" Sua pontuação: {pontuacao}")

    match qntd_numeros:
        case 51:
            tentativa = 10
            tentativa_mostrar = 10
            parametro_pontuacao = 100
        case 101:
            tentativa = 8
            tentativa_mostrar = 8
            parametro_pontuacao = 125
        case 301:
            tentativa = 8
            tentativa_mostrar = 8
            parametro_pontuacao = 100

    while (not ganhou and not perdeu):
        chute = int(input(f"\n Você está na tentativa {tentativa} de {tentativa_mostrar}. Digite seu chute: "))

        if (str(chute) in salvar):
            print(" Você já digitou esse número! Tente outro!")
            continue
        else:
            salvar.append(str(chute))

        if (chute > qntd_numeros - 1 or chute < 0):
            print(f" Por gentileza digite um número entre 0 e {qntd_numeros - 1}")
            continue

        if (chute == numero_secreto):
            print(" Parabéns você acertou!")
            print(f" Sua pontuação: {pontuacao}")
            ganhou = True

        else:
            print(" Você errou.", end=" ")
            tentativa -= 1
            pontuacao -= parametro_pontuacao
            if (chute > numero_secreto):
                print("Você precisa chutar um número menor!")
            else:
                print("Você precisa chutar um número maior!")
            print(f" Sua pontuação: {pontuacao}")
        if (tentativa <= 0):
            print("\n Você perdeu!")
            break

def selecionar_nivel():

    confirmacao = False

    nivel_selecionado = int(input(" Escolha um nível:"))

    while (not confirmacao):

        qntd_numeros = 0

        match nivel_selecionado:
            case 1:
                print(" Nível selecionado FACÍL! (0 até 50)")
                qntd_numeros = 51
                confirmacao = True
            case 2:
                print(" Nível selecionado MÉDIO! (0 até 100)")
                qntd_numeros = 101
                confirmacao = True
            case 3:
                print(" Nível selecionado DIFÍCIL! (0 até 300)")
                qntd_numeros = 301
                confirmacao = True
            case _:
                print(" Selecione um nível valido!")

        if (nivel_selecionado <= 0 or nivel_selecionado >= 4):
            nivel_selecionado = int(input(" Escolha um nível:"))
            continue
    return qntd_numeros

def desenhar_nome_do_jogo():
    print("╔=====================================╗")
    print("║         JOGO DA ADIVINHAÇÃO         ║")
    print("╠=====================================╣")
    print("║ 1 - FACÍL │ 2 - MÉDI0 │ 3 - DIFÍCIL ║")
    print("╚=====================================╝")

if (__name__ == "__main__"):
    jogo_adivinha_numero()