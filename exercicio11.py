#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:

#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)


peso = float(input("Digite seu peso em kg: "))


altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc <= 29.9:
    print("Classificação: Sobrepeso")
else: 
    print("Classificação: Obesidade")



