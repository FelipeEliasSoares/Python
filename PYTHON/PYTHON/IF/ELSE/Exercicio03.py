idade=0
nome=""
Categoria=""

print("------CATEGORIA DE NATAÇÂO-----")
nome =(input("Digite o seu nome: "))
idade = int(input("Informe sua idade: "))

if(idade>=5) and (idade<=7):
    Categoria="INFANTIL A"
elif(idade>=8) and (idade<=11):
    Categoria= "INFANTIL B"
elif(idade>=12) and (idade<=13):
    Categoria="JUVENIL A" 
elif(idade>=14) and (idade<=17):
    Categoria="JUVENIL B"
elif(idade <=18):
    Categoria="ADULTO"
else:
    Categoria="Categoria invalida"

print(f"{nome} sua categoria é {Categoria}")