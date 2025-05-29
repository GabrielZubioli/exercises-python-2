num = int(input("Digite um número que direi se é primo: "))

if num <= 1:
    print("Não é um número primo")
else:
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("É um número primo")
    else:
        print("Não é um número primo")
