# ### Comentário

variavel = 1

print(variavel)

print(type(variavel))

variavel = '1'

print(variavel)

print(type(variavel))

2 < 4
2 > 4
2 <= 4
2 >= 4
2 == 4
2 != 4

False and True
False or True
not True

2 + 2
2 - 2
2 * 2
2 / 2
5 % 2 # Resultado = 1
2 ** 2

(2 + 2) * 2

num1 = 2
num2 = 3

if not ((num1 + num2) > 3):
    print('Verdadeiro')
else:
    print('Falso')

if not ((num1 + num2) < 3):
    print('Verdadeiro')
else:
    print('Falso')

numTotal = 80

# if numTotal > 80:
#     print('Maior que 80')
#     if numTotal > 70:
#         print('Maior que 70')
#     else:
#         print('Menor que 70')

if numTotal > 80:
    print('Maior que 80')
elif numTotal > 70:
    print('Maior que 70')
else:
    print('Menor que 70')

import time

segundo = 0

while segundo < 10:
    # time.sleep(.1)
    segundo = segundo + 1
    print(segundo)

for ru in range(13):
    print(f"Rua {ru+1}")

vetor = ["Rua a", "Rua b","Rua c"]

print(vetor)

for r in vetor:
    print(r)

print('\n')

cidade = [
    ["Rua a", "Rua b","Rua c"],
    ["Rua e", "Rua r","Rua t"],
    ["Rua z", "Rua x","Rua v"],
    ["Rua l", "Rua k","Rua j"]
]

for bairro in cidade:
    ruasDoBairro = ''
    for rua in bairro:
        ruasDoBairro = ruasDoBairro + rua + " "
    print(ruasDoBairro)
