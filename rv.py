##### Revisão #####

# Vetor

# classe list

# 0 1 2 3 4

pessoas = ['Amanda', 'Bruno', 'Carla']
pets = []

pets.append('Totó')
pets.append('Auau')
pets.append('Mimi')

# print(pessoas)
# print(pets)

# for pessoa in pessoas:
#     print(pessoa)

# print(len(pessoas))

# print(pessoas[2])

for i in range(len(pessoas)):
    # print(i, pessoas[i])
    # print(f"Índice: {i} - Valor: {pessoas[i]}")
    pass

veiculos = [
    ['Renegade','Toro','Hilux'],
    ['Cg Titan','Harley-Davidson']
]

for categoria in veiculos:
    for veiculo in categoria:
        pass
        # print(veiculo)

# Objeto

class Automovel:
    nome = ''
    cor = ''
    ano = 0
    ligado = False

    def ligar(self):
        self.ligado = not self.ligado
    
    # Versão 2.0

    def __str__(self):
        return f"Nome: {self.nome} - Cor: {self.cor} - Ano: {self.ano} - Ligado: {'Sim' if self.ligado else 'Não'}"

    def __init__(self, nome = "", cor = "", ano = 0, ligado = False):
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.ligado = ligado



auto = Automovel()

print(auto)
print(auto.cor, auto.ano, auto.ligado)
print(auto.cor, auto.ano, auto.ligado)
print(auto.cor, auto.ano, auto.ligado)
print(auto.cor, auto.ano, auto.ligado)

auto.ligar()

print(auto.cor, auto.ano, auto.ligado)

auto.nome = "Renegade"
auto.cor = "Vermelho"
auto.ano = 2019

print(auto.cor, auto.ano, auto.ligado)

auto.ligar()

print(auto.cor, auto.ano, auto.ligado)

print(auto)

autoOutro = Automovel()

print(autoOutro)

autoMaisOutro = Automovel("Toro", "Branco", 2020)

print(autoMaisOutro)

autoMaisOutroAinda = Automovel(ano=2021, nome="Nivus")


print(autoMaisOutroAinda)

autoMaisOutroAinda.cor = "Branco"

print(autoMaisOutroAinda)

autoMaisOutroAinda.ligar()

print(autoMaisOutroAinda)

class Carro(Automovel):
    chassi = ''
    def __init__(self):
        super().__init__()

class Moto(Automovel):
    numeroDoQuadro = ''
    def __init__(self):
        super().__init__()

carro = Carro()
moto = Moto()

print(carro)
print(moto)



# toggle