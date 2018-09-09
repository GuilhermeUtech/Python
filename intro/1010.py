lista1 = input().split(' ') #transformando em uma lista dividindo nos espaços
lista2 = input().split(' ') #transformando em uma lista dividindo nos espaços
cd1,n1,val1 = lista1 #aplicando o valor das listas
cd2,n2,val2 = lista2
print("VALOR A PAGAR: R$ %.2f" %((int(n1)*float(val1)) + (int(n2)*float(val2)))) #To castando pq como só dei um input normal
#o python considera como se fosse uma str visto que esssa é sua entrada padrão de input
