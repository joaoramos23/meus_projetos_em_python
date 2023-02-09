from collections import Counter

texto1 = """ Por fim, vamos colocar tudo isso em prática para vermos algum exemplo diferente? Então o que eu queria fazer agora não é um contador de palavras, eu fazer um contador de letras para vermos uma coisa interessante que acontece na língua portuguesa e em outras línguas, para ser sincero, também. Então eu vou criar aqui uma nova sessão que é "#Testando o uso de diversas coleções". Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares."""
texto2 = """ ntão dois textos de assuntos totalmente diferentes: vendas, negócio, B2B, B2C; programação, expressão regular, e por aí vai, no caso era até com Java Script e HTML, se não me engano. Então vamos lá. Então eu tenho dois textos que eu queria fazer agora era contar as letras. Será que eu consigo contar as letras de um texto? Então vamos parar para pensar: se eu fizer um for palavra in texto1.split( ):. Quando eu faço o texto1.split( ), o que é o texto1.split( ) mesmo? Ele quebra o texto em palavras. Mas quando tem uma palavra, por exemplo "guilherme", e eu fizer um for x in "guilherme":, cada um dos elementos x é o que? É uma das letras. Então em um texto, você pode considerar, entre aspas, que uma string é como se funcionasse como uma lista ou um iterável de caracteres. Um texto string no Python é um iterável de caracteres, você pode pensar dessa maneira. E já que isso é verdade, aqui da maneira que eu estou trabalhando, então eu poderia criar um contador em cima do texto1.  """

aparicoes = Counter(texto1.lower())
total = sum(aparicoes.values())


tupla = [(letra, valor/total) for letra, valor in aparicoes.items()]
print(tupla)
print("\n")
tupla = dict(tupla)
print("Usando dict: ",tupla)
tupla = Counter(dict(tupla))
print("Usando Counter: ",tupla)
print("")
print((tupla.most_common(10)))
totali = 0

for caractere, valor in tupla.most_common(10):
    totali += valor
print(f"TOTAL = {totali}")

print("\n\n")


def analisando_frequencia(texto):
    aparicoes = Counter(texto.lower())
    total = sum(aparicoes.values())
    total_prop = 0

    proporcao = [(letra, valor/total) for letra, valor in aparicoes.items()]
    proporcao = Counter(dict(proporcao))
    mais_comuns = proporcao.most_common(10)

    for caractere, proporcao in mais_comuns:
        print(f"Letra: {caractere} - {proporcao * 100:,.2f}%")
        total_prop += proporcao
    print(f"TOTAL = {total_prop * 100:,.2f}%")
    print("\n\n")

texto_frase = "Oi meu nome é joao fernando e tenho 3 gatos com nome de maroca nome de billy e nome de faisca, faisca gosta de andar pela casa, billy gosta de dormir e maroca gosta de comer"

analisando_frequencia(texto_frase)

analisando_frequencia(texto1)

analisando_frequencia(texto2)







