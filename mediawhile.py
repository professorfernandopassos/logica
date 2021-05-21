quantidadeDeNotas = input("Quantas notas gostaria de registrar? ")
quantidadeDeNotas = int(quantidadeDeNotas)

contador = 0
acumulador = 0

while(contador < quantidadeDeNotas):
    print(contador,acumulador)
    acumulador = acumulador + 70
    contador = contador + 1

print(acumulador / quantidadeDeNotas)