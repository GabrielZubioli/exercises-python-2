def main():
    intervaloComeco = int(input("Insira o numero que começara o intervalo: "))

    parar = False

    while parar:
        intervaloFinal = int(input("Insira o numero que terminara o intervalo:"))
        if (intervaloFinal - intervaloComeco) > 100:
            parar = True
        intervaloFinal = int(input("Intervalo invalido"))

    somaDoIntervalo = soma(intervaloComeco,intervaloFinal)
    print
    
def soma(intervaloComeco, intervaloFinal):
    resultado = 0
    for i in range (intervaloComeco, up_to, intervaloFinal) :
        resultado = resultado + i
    return resultado


