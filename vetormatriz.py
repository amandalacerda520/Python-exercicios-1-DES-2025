alunos = ["alice", "bruno", "carla"]

dias =["seg", "ter", "qua", "qiu"]

reserva = [["ausente" for _ in dias] for _ in alunos]

print("preencha vom 's' para presença e 'x'para ausência:")

for i, aluno in enumerate(aluno):
    print(f"\naluno: {aluno}")
    for j, dia in enumerate (dias):
        entrada = input(f" {dia}: ")
        if entrada.upper() == 's':
            reservas[i][j] = "presente"

print("\ntabela de reserva:")
print(f"{'aluno':<10}{' '. join(f'{d:<10}' for d in dias )}")
for i, aluno in enumerate (aluno):
    print(f"aluno:<10} {' '.join(f'{res:<10}' for res in reservas[i]])}")