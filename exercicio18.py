 #Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

#Exercício 19 – Números e

# Solicita o salário atual do usuário
salario_atual = float(input("Digite o seu salário atual em R$: "))

# Calcula o reajuste e o novo salário
if salario_atual <= 2000.00:
    percentual_reajuste = 0.15
    reajuste = salario_atual * percentual_reajuste
    novo_salario = salario_atual + reajuste
    print(f"\nVocê terá um reajuste de 15%!")
elif 2000.01 <= salario_atual <= 5000.00:
    percentual_reajuste = 0.10
    reajuste = salario_atual * percentual_reajuste
    novo_salario = salario_atual + reajuste
    print(f"\nVocê terá um reajuste de 10%!")
else:  
    percentual_reajuste = 0.05
    reajuste = salario_atual * percentual_reajuste
    novo_salario = salario_atual + reajuste
    print(f"\nVocê terá um reajuste de 5%!")

# Exibe os resultados
print(f"Valor do reajuste: R$ {reajuste:.2f}")
print(f"Seu novo salário será: R$ {novo_salario:.2f}")