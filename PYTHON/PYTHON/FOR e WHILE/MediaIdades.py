q=0
contador = 0
idade= 0
media = 0.0
soma =0
maior = 0
menor = 0

q = int(input("Digite a quantidade de pessoas: "))
q = q + 1
for contador in range (1,q,1):
    idade = int(input("Qual sua idade: "))
    soma = soma + idade 

    if (contador == 1):
        menor = idade

    if( maior < idade):
        maior = idade

    if(menor > idade):
        menor = idade


media = (soma / q)
print(f"A media das idades foi:{media}")
print(f"A menor idade foi:{menor}")
print(f"A maior idade foi:{maior}")