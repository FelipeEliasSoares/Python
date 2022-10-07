#variavel
contador = 0
numero = 0 

#algoritmo
numero = int(input("Informe o numero para tabuada: "))

for contador in range (1,11,1):
    print(f"{numero} X {contador} = {numero * contador}")