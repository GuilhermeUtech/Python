a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
nove = 0
tupla = a, b, c, d, e
for i in range(0,5):
    if(tupla[i] == 9):
        nove = nove + 1
print("Número de 9: {}".format(nove))
for i in range(0,5):
    if(tupla[i] % 2 == 0):
        print("Par: {}".format(tupla[i]))
for i in range(0,5):
    if(tupla[i] == 3):
        print("Primeira aparição do 3: {}".format(tupla[i]))
        break;




