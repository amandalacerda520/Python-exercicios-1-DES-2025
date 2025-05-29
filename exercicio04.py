# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).


peso = float(input("digite o peso (kg):"))
altura = float(input("digite a altura(m):"))

imc = peso / (altura**2)

  print(f"IMC:{imc:.2f}")

 if imc < 18.5:
   print("Abaixo do peso.")
elif imc < 25:
   print ("Peso normal.")
else:
   print ("acima do peso.")

   
      
