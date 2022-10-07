#Variaveis
ml = 0
ml2= 0
ml3= 0
litros = 0.0

print("Quantidade de litros")
ml = int(input("Quantas latas de 350ml, voce quer: "))
ml2 = int(input("Quantas latas de 600ml, voce quer: "))
ml3 = int(input("Quantas garrafas de 2 litro, voce quer: "))

litros = (ml * (350/1000)) + (ml2 * (600/1000)) + (ml3  * 2)

print (f"A quantidade de litros foi {litros} litros")






