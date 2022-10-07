velocidade_media = 0.0
tempo = 0.0
km_litro = 0.0
distancia = 0.0
litros = 0.0

velocidade_media = float(input("Informe a velocidade media : "))
tempo = float(input("Informe o tempo gasto : "))
km_litro = float(input("Infomer o KM/Litro o carro faz : "))

distancia = velocidade_media * tempo
litros =  tempo * km_litro

print(f"A velocidade_media foi : {velocidade_media}")
print(f"O tempo gasto da viagem foi : {tempo}")
print(f"A distancia foi :{distancia}")
print(f"A quantidade de litros utilizado foi :{litros}")