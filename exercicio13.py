 #Crie um programa que receba um ano e diga se ele é bissexto.
#(Dica: múltiplos de 4, exceto os múltiplos de 100, a menos que também sejam múltiplos de 400)

ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")