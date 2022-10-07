#Variveis
polegada = 0.0
jardas = 0.0
milha = 0.0
pes = 0.0

print ("Conversões de medida")
pes = float(input("Informe a quantiadade de pés :"))

polegada = pes * 12
jardas = pes / 3
milha = jardas / 1760

print(f"A quantidade de pes é {pes}")
print(f"O numero de polegadas é :{polegada}")
print(f"O numero de jardas é : {jardas: 2f}")
print(f"O vaçpr de milha é : {milha: 5f}")



