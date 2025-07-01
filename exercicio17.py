 #Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

# Solicita o salário atual do usuário
salario_atual = float(input("Digite o seu salário atual em R$: "))

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

print(f"Valor do reajuste: R$ {reajuste:.2f}")
print(f"Seu novo salário será: R$ {novo_salario:.2f}")