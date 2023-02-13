class Usuario:

    nome = None
    email = None
    senha = None
    idade = None

    def __init__(self):
        pass

    def nome_email(self):
        return self.nome + " - " + self.email

    def idade_multiplica(self, multi: int=1):
        return self.idade * multi

meu_usuario = Usuario()

meu_usuario.nome = "João"
meu_usuario.email = "joao.fernando.ramos23@gmail.com"
meu_usuario.senha = "12345"
meu_usuario.idade = 23
usuario = meu_usuario.nome_email()
joao = meu_usuario.__dict__

for key,value in joao.items():
    print(f"{key} -> {value}")
print()
print(usuario)
print(meu_usuario.idade_multiplica())
