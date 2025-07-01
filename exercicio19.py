 #Peça três números e exiba-os em ordem crescente.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 <= numero2 and numero1 <= numero3:
    primeiro = numero1
    if numero2 <= numero3:
        segundo = numero2
        terceiro = numero3
    else:
        segundo = numero3
        terceiro = numero2
elif numero2 <= numero1 and numero2 <= numero3:
    primeiro = numero2
    if numero1 <= numero3:
        segundo = numero1
        terceiro = numero3
    else:
        segundo = numero3
        terceiro = numero1
else:
    primeiro = numero3
    if numero1 <= numero2:
        segundo = numero1
        terceiro = numero2
    else:
        segundo = numero2
        terceiro = numero1

print(f"Os números em ordem crescente são: {primeiro}, {segundo}, {terceiro}")