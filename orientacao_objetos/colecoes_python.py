"""
1 - Lista
2 - Tupla
3 - Dicionário
4 - Set
"""

# --- 1 - Lista --- #

lista_de_compras = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Macarrão"
]

print(lista_de_compras)

lista_de_compras.append("Carne")

print(lista_de_compras)

lista_de_compras.remove("Macarrão")

print(lista_de_compras)

# --- 2 - Tupla --- #

tupla = (1,2,6,5,3)

print(tupla)

print(tupla[0])

print(tupla.index(6))

# --- 3 - Dicionário --- #

dicionario = {
    "nome": "João",
    "idade": 30,
    "apelidos": ["Jofe","Jofinho","Joao"],
    "trabalho":  {"cargo": "analista de sistemas"}
}

for keys,value in dicionario.items():
    print(keys, " - ", value)
    dicionario[keys] = "teste"

print(dicionario)

# --- 4 - Set --- #

conjunto_set = {"Joao","Joao","Alan","Marcelo"}
print(conjunto_set)

# --------------------#

duplicadas = ["João","João","Fernando","Fernando"]
print(duplicadas)
print(list(set(duplicadas)))