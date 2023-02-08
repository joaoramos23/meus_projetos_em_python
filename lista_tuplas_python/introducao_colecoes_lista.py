idades = [30,29,18]   #lista
print(type(idades))

for idade in idades:
    print(idade,end=" ")
print()
for idade in range(0,len(idades)):
    print(idades[idade],end=" ")
print()

idades.append(15)
print(idades)

idades.remove(15)
print(idades)

idades.clear()
print(idades)

idades.append(15)
idades.append(45)
idades.append(23)
idades.append(14)
print(idades)

if(23 in idades):
    idades.remove(23)

print(idades)

idades.insert(0,39)
print(idades)

idades.insert(2,28)
print(idades)

idades.extend([30,25,40])
print(idades)

idades_ano_que_vem = [idade + 1 for idade in idades]
print(idades_ano_que_vem)

idade_maior = [idade for idade in idades if idade > 21]
print(idade_maior)

def faz_processamento_de_visualizacao(lista = None):
    if(lista == None):
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(300)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

print(idades)