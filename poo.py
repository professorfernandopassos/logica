# a = "oi"

# print(type(a))

# i = 1

# print(type(i))

# class Pessoa:
#     nome = "Fernando"

# eu = Pessoa()

# # print(type(eu))

# print(eu.nome)

# eu.nome = "Fernando Passos"

# print(eu.nome)

class Pessoa:
    def __init__(self, nome = "", sobrenome = ""):
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return self.nome + " " + self.sobrenome

    def emMaiusculo(self):
        return self.__str__().upper()

eu1 = Pessoa()

print(eu1.nome, eu1.sobrenome)

eu2 = Pessoa("Fernando")

print(eu2.nome, eu2.sobrenome)

eu3 = Pessoa("Fernando", "Passos")

print(eu3.nome, eu3.sobrenome)

eu4 = Pessoa(sobrenome = "Passos")

print(eu4.nome, eu4.sobrenome)

print(eu3)

class Funcionario(Pessoa):
    def __init__(self, matricula = 0):
        self.matricula = matricula
        super().__init__()

func = Funcionario(123456)

print(func.matricula)

# func.nome = "Fernando"

print(eu3.emMaiusculo())