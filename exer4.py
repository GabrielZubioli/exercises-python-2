def saoAnagramas(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")

if saoAnagramas(string1, string2):
    print("São anagramas!")
else:
    print("Não são anagramas.")
