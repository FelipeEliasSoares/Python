caseirinho = 0
broinha = 0
total= 0.0
vbroinha= 0.0
vcaseirinho=0.0
poupança = 0.0

caseirinho = int(input("Informe a quantidade de caseirinho vendidos: "))
broinha = int(input("Informe a quantidade de broinha vendidos: "))

vcaseirinho = (caseirinho * 0.10)
vbroinha = (broinha * 1.60)
total = vbroinha + vcaseirinho
poupança = (total * 0.1)

print(f'A quantidade de caseirinho foi {vcaseirinho:,.2f}')
print(f'A quantidade de broinha foi {vbroinha:,.2f}')
print(f"O toltal das compras foi {total:,.2f}")
print(f"O valor que devera ser guardado sera {poupança:,.2f}")
