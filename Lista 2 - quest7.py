#Lista 2 - quest7


#SOLICITAR INFO
codigo = int(input("Digite o código do item: "))
quantidade = int(input("Digite a quantidade: "))

#VERIFICACAO
if codigo == 100:
    preco_unitario = 18.50
elif codigo == 101:
    preco_unitario = 21.30
elif codigo == 102:
    preco_unitario = 19.20
elif codigo == 103:
    preco_unitario = 22.30
elif codigo == 104:
    preco_unitario = 25.00
elif codigo == 105:
    preco_unitario = 5.00
else:
    print("Código de item inválido.")
    exit()

#CALCULO VAOLOR TOTAL
valor_total = preco_unitario * quantidade

#EXIBICAO
print("O valor total a ser pago é: R$", valor_total)