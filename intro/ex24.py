a = int(input("Reta 1:\n"))
b = int(input("Reta 2:\n"))
c = int(input("Reta 3:\n"))

if(a > (b+c) or b>(a+c) or (c >a+b)):
    print("Não é possível construir um triangulo\n")
else:
    print("Da de construir um triangulo\n")

