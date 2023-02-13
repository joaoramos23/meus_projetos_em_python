class Automovel:

    def __init__(self):
        pass

    def alterar_placa(self,nova):
        self.placa  = nova
        return self.placa

    def Acelerar(self):
        pass

    def Parar(self):
        pass

class Carro(Automovel):
    def __init__(self):
        pass

    combustivel = None
    cor = None
    placa = None

novo_carro = Carro()
novo_carro.combustivel = "Gasolina"
novo_carro.cor = "Vermelho"
novo_carro.placa = "OUO-9091"

exibir = novo_carro.__dict__

for key,value in exibir.items():
    print(f"{key} -> {value}")

print()

novo_carro.alterar_placa("OUO-0909")

for key,value in exibir.items():
    print(f"{key} -> {value}")

