# Douglas está criando uma função simples no jogo que verifica se o número é múltiplo de 2 ou não (par ou ímpar).
# Escreva um programa que faça essa verificação.
numero = int(input("digite seu numero"))

if numero % 2 == 0:
    print(f"o numero: {numero} é par, multiplo de 2,parabens")
else:
    print(f"o numero: {numero} é impar, por tanto não é multiplo de 2")