# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("digite o salario mensal de renata: R$ "))
parcela = float(input("digite o valor da parcela do funcionamento: R$ "))

if salario <= 3000:
    print("financiamento negado, salario abaixo do minimo exigido.")
elif parcela > salario * 0.35:
    print("finaciamento negado,parcela acima de 35% do salario. ")
else:
     print("financiamento aprovado !") 