#variveis
n1=0
n2=0
resultado=0

#funcao
def somar_numeros(numero1,numero2):
    resultado = numero1 + numero2
    print(f"A soma dos numeros é: {resultado}")

#algoritmo principal
n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
somar_numeros(n1,n2)