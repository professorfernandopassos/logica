import time

contador = 0

while(contador < 11):
    print("Contador: " + str(contador) + " Número: " + str(contador+1))
    time.sleep(.500)
    contador = contador + 1
