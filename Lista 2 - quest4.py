#Lista 2 - quest4


#SOLICITAR INFO
preco = float(input("Digite o preço do produto: "))

#CALCULO DESCONTO
desconto = preco * 0.10 #0.10 = 10%

#CALCULO NOVO PRECO
novo_preco = preco - desconto

#EXIBICAO
print("O novo preço do produto com desconto é: R$", novo_preco)