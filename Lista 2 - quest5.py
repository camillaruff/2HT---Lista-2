#Lista 2 - quest5


#SOLICITAR INFO
numero = int(input("Digite um número para a tabuada: "))

#CALCULO TABUADA
for i in range(1, 11): # laço de repetição

    resultado = numero * i

    #EXIBICAO
    print(numero, "x", i, "=", resultado)