class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return (f">> Codigo {self.codigo} Saldo {self.saldo} <<")

conta_do_joao = ContaCorrente(15)
print(conta_do_joao)
conta_do_joao.deposita(500)
print(conta_do_joao)

print()

conta_do_ana = ContaCorrente(47685)
print(conta_do_ana)
conta_do_ana.deposita(1000)
print(conta_do_ana)

print()

contas = [conta_do_joao,conta_do_ana]
for conta in contas:
    print(conta)

conta_do_joao.deposita(200)

print()

print(contas[0])
print(conta_do_joao)
print("\n\n\n")

print(contas[0],contas[1])

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas)

print(contas[0],contas[1])
print()

joao = ("João", 23, 1999) #tuplas
ana = ("Ana", 49, 1973)
# paulo = (39, "Paulo", 1979) ruim #

conta_joao = (15,1000)
print(conta_joao[1])

def deposita(conta):
   novo_saldo = conta[1] + 100
   codigo = conta[0]
   return (codigo,novo_saldo)

print(deposita(conta_joao))
print(conta_joao)

usuarios = [joao,ana]
print(usuarios)

usuarios.append(("Paulo",39,1979))
print(usuarios)

conta_do_joao = ContaCorrente(15)
conta_do_joao.deposita(500)
conta_do_ana = ContaCorrente(47685)
conta_do_ana.deposita(1000)

contas = (conta_do_joao,conta_do_ana)
print()
for conta in contas:
    print(conta)
print()
contas[0].deposita(200)
for conta in contas:
    print(conta)
print("\n\n\n")

#HERANÇA E POLIMORFISMO#
from abc import ABCMeta, abstractmethod
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    @abstractmethod
    def passa_o_mes(self):
        pass
    def __str__(self):
        return (f">> Codigo {self._codigo} Saldo {self._saldo} <<")


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
class ContaInvestimento(Conta):
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta18 = ContaInvestimento(88) #se eu tentar instanciar não vai por não implementar metodo abstrato.


contas = [conta16,conta17]

for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)

#array, evitaremos usar. Se precisamos de trabalho numerico usar numpy!

import array as arr

print(arr.array("d",[1,3.5]))

import numpy as np

numeros = np.array([1,3.5])
print(numeros + 3)
print(type(numeros))
