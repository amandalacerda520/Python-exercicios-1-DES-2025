#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
dia01 = int(input("digite o tempo nessecario para entregar a atividade x "))
dia02 = int(input("Digite o tempo necessário para entregar a atividade y")) 
dia03 = int(input("Digite o tempo  necessário para entregar a atividade z"))

if dia01 < 0 or dia02 < 0 or dia03 < 0:
    print("erro negativo.")
else:
    soma = dia01 + dia02 + dia03
    print(f"tempo total da atividade: {soma} dias ")