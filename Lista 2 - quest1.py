#Lista 2 - quest1


#SOLICITAR INFO
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
ano_futuro = int(input("Digite o ano que você deseja saber qual seria a sua idade"))

#CALCULO IDADE ATUAL
idade_atual = ano_atual - ano_nascimento

#CALCULO IDADE FUTURA
idade_futura = ano_futuro - ano_nascimento

#EXIBICAO
print("Idade atual:", idade_atual, "anos")
print("Idade em 2099:", idade_futura, "anos")