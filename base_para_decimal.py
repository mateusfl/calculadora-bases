hexa_dict = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def base_para_decimal(valor: str, base: int):
    valor = valor.upper()

    antes_da_virgula = valor.split(".")[0]
    try:
        depois_da_virgula = valor.split(".")[1]
    except:
        depois_da_virgula = ["0"]

    lista_0 = list(antes_da_virgula)
    lista_1 = list(depois_da_virgula)
    lista_0_decimal = []
    lista_1_decimal = []

    # Convertendo a parte inteira (0)
    for i in range(len(lista_0)):
        try:
            lista_0_decimal.append(int(lista_0[i]))
        except:
            for j in range(len(hexa_dict)):
                if lista_0[i] == list(hexa_dict.keys())[j]:
                    lista_0_decimal.append(list(hexa_dict.values())[j])

    # Convertendo a parte fracionária (1)
    for i in range(len(lista_1)):
        try:
            lista_1_decimal.append(int(lista_1[i]))
        except:
            for j in range(len(hexa_dict)):
                if lista_1[i] == list(hexa_dict.keys())[j]:
                    lista_1_decimal.append(list(hexa_dict.values())[j])

    resultado = 0
    exp = len(lista_0_decimal) - 1
    for i in range(len(lista_0_decimal)):
        resultado += lista_0_decimal[i] * pow(base, exp)
        exp -= 1

    for i in range(len(lista_1_decimal)):
        resultado += lista_1_decimal[i] * pow(base, exp)
        exp -= 1

    return resultado
