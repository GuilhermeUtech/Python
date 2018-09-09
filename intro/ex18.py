vel = int(input("Digite a velocidade\n"))
if(vel > 80):
    print("Você foi multado no valor de R$ {}\n".format(7*(vel-80)))
else:
    print("Tudo tranquilo jovem!\n")