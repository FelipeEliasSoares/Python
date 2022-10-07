#variaveis 
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#algoritmo
nome = input("Infome o NOME do aluno : ")
nota1 = float(input("Informe a nota 1 : "))
nota2 = float(input("informe a nota 2 : "))
media = (nota1 + nota2) / 2 


print(f"{nome}, a sua media é: {media}")
