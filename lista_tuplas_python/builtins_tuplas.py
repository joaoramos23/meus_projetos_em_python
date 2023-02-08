idades = [15,87,32,65,56,32,49,37]

for i in range(len(idades)):
    print(f"/{i} - {idades[i]}/",end="")

print()
print(list(range(len(idades))))
print(f"\n{enumerate(idades)}")
print(list(enumerate(idades)))

for indice,valor in enumerate(idades):
    print(indice," x ",valor)


usuarios = [("Guilherme",37,1981),("Daniela", 31, 1987),("Paulo", 39,1979)]
usuarios_codigos = list(enumerate(usuarios))
print(usuarios_codigos)

escolha = int(input("Escolha o codigo do usuarios: "))

for codigo,usuario in usuarios_codigos:
    if codigo == escolha:
        print(usuario)


print("\n\n")
for nome,idade,data in usuarios: #ja desempacotando
    print(nome,data)

print()

for nome,_,_ in usuarios: #ja desempacotando
    print(nome)


