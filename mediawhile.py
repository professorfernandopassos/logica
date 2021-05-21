
# Serve para guardar a quantidade de notas que eu quero coletar
quantidadeDeNotas = input("Quantas notas gostaria de registrar? ")
quantidadeDeNotas = int(quantidadeDeNotas)

# Contar a quantidade de vezes que a repetição já aconteceu
contador = 0

# Serve para guardar as somas das notas fornecidas
acumulador = 0

while(contador < quantidadeDeNotas):
    nota = input("Insira a nota " + str(contador+1) + ": ")
    nota = int(nota)
    acumulador = acumulador + nota
    contador = contador + 1
    
media = acumulador / quantidadeDeNotas

if(media >= 70):
    print(f"Sua média foi de {int(media)}. Boas férias!")
elif(media >=50):
    print(f"Sua média foi de {int(media)}. Você está em recuperação.")
else:
    print(f"Sua média foi de {int(media)}. Você foi reprovado.")