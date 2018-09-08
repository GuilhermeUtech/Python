a = str(input("Digite seu nome completo.\n"))
print("O seu nome com todas as letras maisculas é: {}".format(a.upper()))

aux = len(a)
nEspaço = a.count(' ')
print(("O número de caracteres sem espaço é de: {}".format(aux-nEspaço)))
aux = a.split()
print(aux)
aux2 = len(aux[0])
print("O tamanho do primeiro nome é de: {}".format(aux2))





