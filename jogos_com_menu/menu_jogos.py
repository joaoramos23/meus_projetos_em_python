# MENU PARA ABRIR JOGOS POR MEIO DO IMPORT #
# OS JOGOS DA FORCA E DA ADIVINHAÇÃO ESTÃO DIFERENTES DOS ANTERIORES #
# FOI ADICIONADO UM ARQUIVO .TXT PARA SALVAR AS PALAVRAS QUE SERÃO USADAS NO JOGO #
# by: João Ramos #

import os
import forca
import adivinhacao
import funcoes

def escolha_jogos():
    funcoes.estrelinha_frase("       Escolha seu jogo:\n       (1) - Forca\n       (2) - Adivinhação")
    escolha = int(input())
    match escolha:
        case 1:
            print("Iniciando jogo da Forca!\n\n")
            forca.jogar_forca()
        case 2:
            print("Iniciando jogo da Adivinhação!\n\n")
            adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogos()