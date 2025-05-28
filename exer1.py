def main():
    intervaloComeco = int(input("Insira o número que começará o intervalo: "))

    while True:
        intervaloFinal = int(input("Insira o número que terminará o intervalo: "))
        if (intervaloFinal - intervaloComeco) > 100:
            break
        else:
            print("Intervalo inválido. A diferença deve ser maior que 100.")

    somaDoIntervalo = soma(intervaloComeco, intervaloFinal)
    print(f"Intervalo informado: {intervaloComeco} a {intervaloFinal}")
    print(f"A soma do intervalo é {somaDoIntervalo}")


def soma(intervaloComeco, intervaloFinal):
    resultado = 0
    for i in range(intervaloComeco, intervaloFinal + 1):
        resultado += i
    return resultado


if __name__ == "__main__":
    main()
