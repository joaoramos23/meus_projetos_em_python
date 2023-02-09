from collections import defaultdict

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito e de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
meu_texto = meu_texto.split()

aparicoes = defaultdict(int)

# usando com objetos #

class Conta:
    def __init__(self):
        print("Criando uma conta.")

contas = defaultdict(Conta)

contas[15]
contas[17]
contas[15]
print(contas)


# counter #

from collections import Counter

aparicoes = Counter(meu_texto)

print(aparicoes)