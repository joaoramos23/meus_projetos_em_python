class CadastroPessoa:
    def __init__(self,nome):
        self.nome = nome

    def cadastrar_idade(self,idade):
        self.idade = idade

    def __str__(self):
        return (f"\nNome: {self.nome}\nIdade: {self.idade}")


cadastro_joao = CadastroPessoa("João Fernando Santo Ramos")
cadastro_joao.cadastrar_idade(23)

cadastro_marileide = CadastroPessoa("Marileide de Jesus Santos")
cadastro_marileide.cadastrar_idade(49)

print(cadastro_joao)
print(cadastro_marileide)

cadastros = [cadastro_joao,cadastro_marileide]

for cadastro in cadastros:
    print(cadastro)