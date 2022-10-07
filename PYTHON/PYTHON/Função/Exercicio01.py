numero = 0
maior_a = 0
menor_a = 0
contador = 0
maior = 0 
menor = 0

def maior(numero,contador,maior):
    if (contador == 1):
        maior = numero
    else:
        if(numero >= maior):
            maior = numero
    return  maior

def menor(numero,contador,menor):
    if (contador == 1):
        menor = numero
    else:
        if(numero <= menor):
            menor = numero
    return  menor



for contador in range(0,5,1):
    numero = int(input("Digite o numero: "))
    maior_a = maior(numero,contador,menor_a)
    menor_a = menor(numero,contador,maior_a)


print(f"O maior numero foi  {maior_a}")
print(f"O menor numero foi  {menor_a}")