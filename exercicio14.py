 #Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

valor_compra = float(input("Digite o valor total da compra em R$: "))


if valor_compra > 500:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"\nVocê teve um desconto de 10%!")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
elif valor_compra > 300:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"\nVocê teve um desconto de 5%!")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
else:
    valor_final = valor_compra
    print(f"\nVocê não teve desconto.")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")