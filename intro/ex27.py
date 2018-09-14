from random import randint

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
tupla = a, b, c, d, e
print(tupla)
maior = a
menor = a
for i in range(0,5):
    if(tupla[i] > maior):
        maior = tupla[i]
    if(tupla[i] < menor):
        menor = tupla[i]
print(maior)
print(menor)