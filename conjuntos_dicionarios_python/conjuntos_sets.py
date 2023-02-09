usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]


assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)
print(len(assistiram))

for usuario in set(assistiram):
    print(usuario,end=" ")

assistiram = set(assistiram)  # fazer um conjunto para tirar elementos repitidos

print(assistiram)
print(len(assistiram))

print({1,3,5,4,2,4,3,7,5,7}) #chamar conjunto simples apenas com colchetes

# chamando conjunto com {} #
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

numeros1 = {1,3,5,7,9}
numeros2 = {3,4,6,7,9}
numeros_uniao = numeros1 | numeros2
numeros_intersecao = numeros1 & numeros2

print(f"\n{numeros_uniao}")
print(numeros_intersecao)
print("\n")

conjunto_data_science = set(usuarios_data_science)
conjunto_machine_learning = set(usuarios_machine_learning)

usuario_data_nao_machine = conjunto_data_science - conjunto_machine_learning
print(usuario_data_nao_machine)
usuario_data_nao_machine = conjunto_machine_learning - conjunto_data_science
print(usuario_data_nao_machine)
a = 56

if(a in conjunto_data_science or a in conjunto_machine_learning):
    if(a in conjunto_data_science - conjunto_machine_learning):
        print("SIM")
    else:
        print("NÃO")
else:
    print("NÃO EXISTE ESSE NUMERO EM NENHUMA LISTA!")

print(usuarios_machine_learning)
print(usuarios_data_science)
print(conjunto_machine_learning ^ conjunto_data_science)
print(conjunto_data_science ^ conjunto_machine_learning)

# MODIFICAR O CONJUNTO EM TEMPO REAL #
print("\n\n")
usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))
usuarios.add(13)
print(len(usuarios))
usuarios.add(765)
print(len(usuarios))

#CONJUNTO IMUTAVEL#
usuarios = frozenset(usuarios)
print(type(usuarios))
#usuarios.add(65)  -> NÃO PODE ADD POIS É UM FROZENSET#

#CONJUNTOS COM STRINGS#
print("\n\n")
meu_texto = "Bem vindo meu nome e João e eu gosto de nomes e de animais"
meu_texto = meu_texto.split()
print(meu_texto)
meu_texto = set(meu_texto)
print(meu_texto)

# DICIONARIOS #
print("\n")

aparicoes = {
    "Joao" : 1,
    "nome" : 2,
    "de" : 3
}

# outra forma #

aparicoes = dict(Joao = 1, nome = 2, de = 3)


print(type(aparicoes))
print(aparicoes["Joao"])
print(aparicoes.get("xpto",0))
print(aparicoes.get("de",0))

print("")
# atribuir valores #
aparicoes["Joao"] = 3
print(aparicoes["Joao"])


print("")
# remover #
print(aparicoes)
del aparicoes["Joao"]
print(aparicoes)

print("")
# verificar se tem dentro #
if("nome" in aparicoes):
    print("True")
else:
    print("False")


print("")
# passar por todos elementos do dict #
for i in aparicoes.keys():
    print(i,"->",aparicoes[i])

for i in aparicoes:
    print(i,"->",aparicoes[i])

for chave,valor in aparicoes.items():
    print(chave,"->",valor)


print("")

# passar pelos valores #
for i in aparicoes.values():
    print(i)

print("")
# exemplos #

print([f"Palavra: {chave} - Valor: {valor}" for chave,valor in aparicoes.items()])

