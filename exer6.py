def calcular_troco_otimo(valor, moedas):
    if valor < 0:
        return "Erro: valor de troco não pode ser negativo."

    dp = [float('inf')] * (valor + 1)
    dp[0] = 0
    caminho = [0] * (valor + 1)

    for i in range(1, valor + 1):
        for moeda in moedas:
            if i >= moeda and dp[i - moeda] + 1 < dp[i]:
                dp[i] = dp[i - moeda] + 1
                caminho[i] = moeda

    if dp[valor] == float('inf'):
        return "Não é possível gerar o troco exato com as moedas fornecidas."

    resultado = []
    atual = valor
    while atual > 0:
        resultado.append(caminho[atual])
        atual -= caminho[atual]

    return resultado

try:
    valor = int(input("Digite o valor do troco: "))
    moedas_input = input("Digite as moedas disponíveis separadas por vírgula (ex: 1,5,10,25,100): ")
    moedas = list(map(int, moedas_input.split(',')))

    resultado = calcular_troco_otimo(valor, moedas)

    print("\nResultado:")
    print(f"O menor número de moedas para {valor} é: {resultado}")

except ValueError:
    print("Erro: Digite apenas números inteiros válidos.")
