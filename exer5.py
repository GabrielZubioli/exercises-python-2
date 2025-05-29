def validar_sudoku(tabuleiro):
    erros = []

    for i in range(9):
        numeros = {}
        for j in range(9):
            num = tabuleiro[i][j]
            if num != 0:
                if num in numeros:
                    erros.append((i, j))
                    erros.append((i, numeros[num]))
                else:
                    numeros[num] = j

    for j in range(9):
        numeros = {}
        for i in range(9):
            num = tabuleiro[i][j]
            if num != 0:
                if num in numeros:
                    erros.append((i, j))
                    erros.append((numeros[num], j))
                else:
                    numeros[num] = i

    for bloco_i in range(3):
        for bloco_j in range(3):
            numeros = {}
            for i in range(bloco_i * 3, bloco_i * 3 + 3):
                for j in range(bloco_j * 3, bloco_j * 3 + 3):
                    num = tabuleiro[i][j]
                    if num != 0:
                        if num in numeros:
                            erros.append((i, j))
                            erros.append(numeros[num])
                        else:
                            numeros[num] = (i, j)

    erros = list(set(erros))

    return erros

tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 5, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 5, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 3, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

erros = validar_sudoku(tabuleiro)

if erros:
    print("Foram encontrados erros nas seguintes células (linha, coluna):")
    for linha, coluna in erros:
        print(f"({linha + 1}, {coluna + 1})")
else:
    print("O tabuleiro está válido!")
