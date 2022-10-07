salarioMinimo = 0.0
salarioMes=0.0
salarioLiquido = 0.0
imposto = 0.0
horatrabalhadas= 0 
salarioBruto = 0.0
valorHora = 0.0
dependentes = 0
horasExtra = 0.0

salarioMinimo = float(input("Digite o seu salario minimo: "))
horatrabalhadas = int(input("Digite as horas trabalhadas: "))
horasExtra = float(input("Digite as horas extras: "))
valorHora = (salarioMinimo/5)
salarioMes = horatrabalhadas * valorHora


dependentes = int(input("Quantos depententes voçe tem:"))
dependentes = dependentes * 32

horasExtra = horasExtra * (valorHora * 1.5)

salarioBruto = salarioMes + dependentes + horasExtra

if (salarioBruto< 200):
    imposto = 0
elif(salarioBruto>200)and(salarioBruto<=500):
    imposto = (salarioBruto * 0.10)
elif(salarioBruto>500):
    imposto = (salarioBruto * 0.20)

salarioLiquido = salarioBruto - imposto

if(salarioLiquido<=350):
    salarioLiquido = salarioLiquido + 100
elif(salarioLiquido>350):
    salarioLiquido = salarioLiquido + 50

print (f"O salario final é R${salarioLiquido:,.2f}")




