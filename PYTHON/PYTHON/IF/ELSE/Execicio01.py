TdC = ""
CdT = 0
preco = 0.0
valor = 0.0

print("Informe o tipo do carro \n G - gasolina ou A - álcool")
TdC = input("Infome: ")
CdT = float(input("Digite a capacidade do tanque:"))

if(TdC.upper == "G"):
    print("Voce escolheu Gasolina")
    preco = float(input("Informe o preço: "))
    valor = preco * CdT

else:
        print= ("Voce escolheu Alcool")
        preco = float(input("Informe o preço: "))
        valor = preco * CdT

print(f"O valor para encher o tanque é R${valor}")
