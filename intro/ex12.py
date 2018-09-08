a = str(input("Digte um número de 0 a 9999\n"))
aux = len(a)

if(aux == 4):
    print("Milhar: {}".format(a[3]))
    print("Centena: {}".format(a[2]))
    print("Dezena: {}".format(a[1]))
    print("Unidade: {}".format(a[0]))

if(aux == 3):
    print("Centena: {}".format(a[2]))
    print("Dezena: {}".format(a[1]))
    print("Unidade: {}".format(a[0]))


if(aux == 2):
    print("Dezena: {}".format(a[1]))
    print("Unidade: {}".format(a[0]))


if(aux == 1):
    print("Unidade: {}".format(a[0]))


