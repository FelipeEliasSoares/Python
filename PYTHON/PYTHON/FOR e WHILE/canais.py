canal = 0
canal_9 = 0.0
qtd9 = 0
canal_12 = 0.0
qtd12 = 0
canal_23 = 0.0
qtd23 = 0
canal_40 = 0.0
qtd40 = 0
outros = 0.0
qtdO= 0
total = 0
while canal !=1 :
    canal = int(input("Informe o canal para pesquisa podendo ser (9,12,23,40) e caso queria finalizar digite 0: "))
    
    if(canal == 0):
        canal += 1
    elif(canal == 9):
        qtd9 += 1
    elif(canal == 12):
        qtd12 += 1
    elif(canal == 23):
        qtd23 += 1 
    elif(canal == 40):
        qtd40 += 1 
    else :
        qtdO += 1

total = qtd9 + qtd12 + qtd23 +  qtd40 + qtdO
canal_9 = (qtd9/total) * 100
canal_12 = (qtd12/total) * 100
canal_23 = (qtd23/total)* 100
canal_40 = (qtd40/total)*100
outros = (qtdO/total)*100

print(f"A portagem de audiencia do canal 9:{canal_9:,.2f}%")
print(f"A portagem de audiencia do canal 12:{canal_12:,.2f}%")
print(f"A portagem de audiencia do canal 23:{canal_23:,.2f}%")
print(f"A portagem de audiencia do canal 40:{canal_40:,.2f}%")
print(f"A portagem de audiencia do outros canais:{outros:,.2f}%")

