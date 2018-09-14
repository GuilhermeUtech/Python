tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
entrada = 0
while(entrada == 0):
    a = int(input("Digite um valor de 0 até 20\n"))
    if(a >= 0 and a <= 20):
        entrada = 1
print("O valor que você escolhue por extenço é: {}".format(tupla[a]))

