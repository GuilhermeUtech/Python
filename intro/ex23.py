n = float(input("Digite seu salário\n"))

if(n>1250):
    print("Seu novo salário é de: R$ {}".format(n+(n*0.10)))
else:
    print("Seu novo salário é de: R$ {}".format(n+(n*0.15)))