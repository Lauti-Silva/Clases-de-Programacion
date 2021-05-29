#! 3:
from random import randint

lista100 = []
lista001 = lista100

for i in range (0,100):
    numero = randint(0,100)
    lista100.append(numero)
print("La lista generada es:")
print(lista100)

lista100.sort()

#! 3-a:
print("Valores indicados: ", lista100[0], lista100[99])
print("La diferencia entre el mayor y el menor es: ", lista100[0] - lista100[99])

#! 3-b:
print(sum(lista100) / 100)

#! 3-c:
print("Lista en orden creciente: ", lista100)

lista001.sort(reverse=True)

#! 3-d:
print("Lista en orden decreciente: ", lista001)

#! 3-e:
for num in lista100:
    if(num % 3 > 0 and num % 2 > 0):
        print(num)
