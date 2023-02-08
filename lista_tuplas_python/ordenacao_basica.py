usuarios = [("Guilherme",37,1981),("Daniela", 31, 1987),("Paulo", 39,1979)]
idades = [15,87,32,65,56,32,49,37]

print(idades)
print(list(reversed(idades)))
print(sorted(idades))
print(sorted(idades,reverse=True))
idades.sort()
print(idades)

print("\n\n")

nomes = ["Guilherme","Daniela","Paulo"]
print(nomes)
print(sorted(nomes))

print("\n\n")

from functools import total_ordering #impotar para ter >= ou <=

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposito(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro.codigo and self._saldo == outro._saldo
    def __lt__(self, outro):
        if(self._saldo == outro._saldo):
            return self._codigo < outro._codigo
        return self._saldo < outro._saldo

    def __str__(self):
        return (f">>Codigo: {self._codigo} Saldo: {self._saldo}<<")


conta_guilherme = ContaSalario(170)
conta_guilherme.deposito(500)
conta_daniela = ContaSalario(3)
conta_daniela.deposito(550)
conta_paulo = ContaSalario(133)
conta_paulo.deposito(1300)

contas = [conta_guilherme,conta_daniela,conta_paulo]

for conta in contas:
    print(conta)

print()

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key= extrai_saldo):
    print(conta)

print()

from operator import attrgetter

for conta in sorted(contas, key= attrgetter("_saldo","_codigo")):
    print(conta)

print()

for conta in sorted(contas):
    print(conta)

print(conta_guilherme >= conta_daniela)