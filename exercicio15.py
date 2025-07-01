 #Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("Por favor, digite sua idade: "))


if idade >= 13:
    print("\nVocê pode se cadastrar no site! Bem-vindo(a)!")
else:
    print("\nDesculpe, você não tem idade suficiente para se cadastrar neste site.")