#Lista 2 - quest10


#SOLICITAR INFO
numero = int(input("Digite um número de 1 a 6: "))

#LISTA
numeros_extenso = [
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis"
]

#VERIFICACAO
if numero >= 1 and numero <= 6:
    #NUMERO EXTENSO
    extenso = numeros_extenso[numero - 1]

    #EXIBICAO
    print("O número", numero, "por extenso é:", extenso)
else:
    print("Número inválido. Digite um número de 1 a 6.")