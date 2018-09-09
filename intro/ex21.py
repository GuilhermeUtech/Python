#Anos bissextos algoritmo dale dele dili dpolu lifo etd 88,12 as ==23
ano = int(input("Digite um ano\n"))
if(ano % 4 == 0):
    if(ano % 100 and ano % 400 != 0):
        print("é")
else:
    print("não é")