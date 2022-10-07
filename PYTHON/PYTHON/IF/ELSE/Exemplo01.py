#variavel
nome = ""
situação = ""
nota01 = 0.0
nota02 = 0.0
media = 0.0

#algoritmo
nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Inform  a nota 2: "))

media = (nota1 + nota2) / 2

if(media >= 6):
    situação = "Aprovado"
else:
    if(media >=4) and (media < 6):
        situação = "Recuperação"
    else:
        situação = "Reprovado"

print(f"{nome}a sua media é: {media} e você está {situação}")    