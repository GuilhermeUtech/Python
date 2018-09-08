a = str(input("Digite uma cadeia de caracteres\n"))
#printando a string
print(a)

b = "Curso em Vídeo Python"
#fatiando a palavra, vou printar do 9 até (21-1) pulando de 2 em 2
print(b[9:21:2])
# vai do inicio até o 5, como eu emiti ele começa do começo
print(b[:5])
#vai printar do 15 até o final
print(b[15:])
#vai printar do 9 até o final pulando 3 em 3
print(b[9::3])
#análise das strings - len
print(len(b)) #tamanho(comprimeot da string)
print(b.count('o')) #contando quantas letras 'o' tem na frase
print(b.count('o', 0,13)) # indo do 0 -> (13-1) contando o número de 'o'
print(b.find('deo')) #Mostra aonde começou (posição) da cadeia deo se retornar -1 é pq n existe
print('Curso' in b)  #retorna true or false

b.replace('Python', 'Video')
print(b.replace('Python', 'Video'))


print(b.upper()) #transforma em maíusculo o que nao é
print(b.lower()) #transforma em minusculo o que n é
print(b.capitalize()) #Só o 1 caractere fica em maisuculo
print(b.title()) #é o capitalize só que palavra por palavra

c = "   Aprenda Python  " #atencao nos espaços vazios
print(c.strip()) #tira espaços inúteis posso usar rstrip pra tira os a direita e o lstrip para tirar os da esquerda

#Divisão de strings

c.split()#estudar essa função divide pelo espaço as palavras
print(c)
'-'.join(c)#juntando as palavras que eu separei utilizando a '-'
print(c)











