def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("Não existe fatorial de número negativo.")
else:
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
