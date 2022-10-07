qtd=0

qtd = int(input("Informe a quantidade: "))

if(qtd <= 10):
    print("Rochosa")
elif(qtd >10 ) and (qtd <=40):
    print("Firme")
elif(qtd > 40) and (qtd <=80):
    print("Pantanoso")
else:
    print("Quantidade de agua invalida!!!")

