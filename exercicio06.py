# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
horariodeacesso = int(input("horario de acesso permitido"))

if 9 <= horariodeacesso <= 21:
 print("a plataforma vesta funcionado perfeitamente.")
else:
    print("plataforma esta fora do horario de funcionamento" ) 
