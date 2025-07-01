#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

idade = int(input("Por favor, digite sua idade: "))

if idade >= 13:
    print("\nVocê pode se cadastrar no site! Bem-vindo(a)!")
else:
    print("\nDesculpe, você não tem idade suficiente para se cadastrar neste site.")

