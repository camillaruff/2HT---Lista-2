#Lista 2 - quest8


#SOLICITAR INFO
numero = int(input("Digite um número de 1 a 7: "))

#LISTA SEMANA
dias_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]

#VERIFICACAO
if numero >= 1 and numero <= 7:
    #DIA DA SEMANA
    dia_semana = dias_semana[numero - 1]

    #EXIBICAO
    print("O dia da semana correspondente ao número", numero, "é:", dia_semana)
else:
    print("Número inválido. Digite um número de 1 a 7.")