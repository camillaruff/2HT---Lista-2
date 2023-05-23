#Lista 2 - quest9


#SOLICITAR INFO
mes = int(input("Digite um valor correspondente ao mês do ano (1 a 12): "))

#VERIFICACAO
if mes in [1, 2, 3]:
    estacao = "Verão"
elif mes in [4, 5, 6]:
    estacao = "Outono"
elif mes in [7, 8, 9]:
    estacao = "Inverno"
elif mes in [10, 11, 12]:
    estacao = "Primavera"
else:
    print("Valor inválido. Digite um valor de 1 a 12 correspondente ao mês do ano.")
    exit()

#EXIBICAO
print("A estação correspondente ao mês", mes, "é:", estacao)