def incremento(numero):
    numero = numero + 1
    return numero

num = incremento(3)

print(num)

print(incremento(1000))

def expo(base, expoente):
    if type(base) == type("") or type(expoente) == type(""):
        print("Precisa ser número")
    else:
        return base ** expoente

print(expo(2,8))

b = input("Digite a base: ")
b = int(b)

e = int(input("Digite o expoente: "))

print(expo(b, e))