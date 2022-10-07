salario=0.0
salarioF=0
bonificacao=0.0
auxilio=0

salario = float(input("Informe o seu salario: "))

if(salario < 500):
    bonificacao= salario * (5/100)
elif(salario >= 500) and (salario <=1200):
    bonificacao= salario * (12/100)
else:
    bonificacao = 0

if(salario <= 600):
    auxilio = 150
else:
    auxilio = 100

salarioF = salario + bonificacao + auxilio
print(f"O seu salario sera de {salarioF}")