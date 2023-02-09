meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito e de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
meu_texto = meu_texto.split()
aparicoes = {}

for palavra in meu_texto:
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

# usando default_dict -> valores padroes#

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto:
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

nomes = "Joao Thiago Carlos"
nomes = nomes.split()
atribuir = defaultdict(int)

for palavra in nomes:
     a = input(f"Digite o valor para {palavra}: ")
     if(not a.isnumeric()):
         a = 0
         atribuir[palavra] = a
     else:
         a = int(a)
         atribuir[palavra] = a

print(atribuir)
print(atribuir["Carlos"])