##################Comentário##################

# Estruturas de Controle - Decisão

# Variaveis recebem os valores
# nota1 = input("Insira a primeira nota: ")
# nota2 = input("Insira a segunda nota: ")
# nota3 = input("Insira a terceira nota: ")

# intNota1 = int(nota1)
# intNota2 = int(nota2)
# intNota3 = int(nota3)

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

# nota1 = input("Insira a primeira nota: ")
# nota2 = input("Insira a segunda nota: ")
# nota3 = input("Insira a terceira nota: ")

# nota1 = int(nota1)
# nota2 = int(nota2)
# nota3 = int(nota3)

# print(type(intNota1), type(intNota2), type(intNota3))

# Variável média recebe o calculo da media das tres notas
# media = (intNota1 + intNota2 + intNota3) / 3
media = (nota1 + nota2 + nota3) / 3

# Decide se o aluno está de férias ou não
if media >= 70:
    print("Sua média foi de " + str(media) + ". Boas férias.")
elif media >= 50:
    # Else-If - Senão-Se
    print("Sua média foi de %d. Você está em recuperação." % media)
else:
    print(f"Sua média foi de {int(media)}. Você está reprovado")
    
