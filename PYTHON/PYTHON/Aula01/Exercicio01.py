#Variaveis
salariobase = 0.0
imposto = 0
salarioF = 0

salariobase = float(input("Informe o seu salario: "))

salariobase = salariobase + 50
imposto = (salariobase * 0.10)
salarioF = salariobase - imposto

print(f"O salario a receber é R$ {salarioF}")