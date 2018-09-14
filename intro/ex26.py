tupla = ('Internacional', 'São Paulo', 'Palmeiras', 'Flamengo', 'Atlético Mineiro', 'Grêmio', 'Cruzeiro', 'Santos', 'Fluminense', 'Corinthians', 'América Mineiro', 'Vitória', 'Bahia', 'Atlético Paranaense', 'Botafogo', 'Vasco da Gama', 'Sport', 'Ceará', 'Chapecoense', 'Paraná')
print("Os primeiros 5 primeiros colocados são: {}".format(tupla[0:5]))
print("Os 4 ultimos colocados são: {}".format(tupla[16:]))
print("Os times por ordem alfabética são: {}".format(sorted(tupla)))

for i in range(0,20):
    if(tupla[i] == "Chapecoense"):
        posi = i
print("A chapecoense está em: {} posição".format(posi))
