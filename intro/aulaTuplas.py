lanche = 'pudin', 'mamão', 'banana', 'maça', 'mandioca'   #TUPLAS SÃO ENTRE PARÊNTESES E SÃO IMUTÁVEIS e não precisam de parênteses kkk
print(lanche)
print(lanche[1])
print(lanche[-2])

#Relembrando fatiamento: na linha print(lanche[1:3]) ele vai printar o 1 e o 2, o 3 ignora
print(lanche[1:3])
#se eu fizer print(lanche[2:) vai printar do 2 at[é o final
print(lanche[2:])

#lanche[1] = 'corote'
#print(lanche[1]) CVAI DAR ERRO, TUPLAS SÃO IMUTÁVeis

for comida in lanche:
    print("eu vou comer {}".format(comida))
print("Comi mt!\n")

print(sorted(lanche)) # nao mudei a tupla mas eu to printando ela em ordem alfabética



