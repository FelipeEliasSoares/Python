preco_fabrica = 0.0
imposto=0.0
lucro = 0.0
valorf=0.0 
percentual_lucro_distribuidor = 0.0

percentual_lucro_distribuidor = float(input("Informe o percentual :"))
preco_fabrica= float(input("Informe o preco do carro : "))

imposto = (percentual_lucro_distribuidor * preco_fabrica)
lucro = preco_fabrica * percentual_lucro_distribuidor
valorf = (preco_fabrica + imposto + lucro)
print(f"O valor final é {valorf}")