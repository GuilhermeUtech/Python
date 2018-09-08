a = str(input("Digite seu nome completo"))
aux = a.split()
print(aux)

aux2 = len(aux)
print(aux2)
print("Primeiro nome: {}".format(aux[0]))
print("Ultimo nome: {}".format(aux[aux2-1]))