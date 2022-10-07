hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def decimal_para_base(valor: str, base: int):
    # convertendo a parte inteira (divisões sucessivas)
    valor_inteiro = int(valor.split(".")[0])

    restos = []

    if valor_inteiro == 0:
        restos.append(0)

    while valor_inteiro > 0:
        restos.append(valor_inteiro % base)
        valor_inteiro = int(valor_inteiro / base)

    restos.reverse()

    restos_string_int = str()
    for i in restos:
        restos_string_int += hexa[i]

    # convertendo a parte fracionária (multiplicações sucessivas)
    valor_fracionario = float(valor) - int(valor.split(".")[0])

    continuar = True
    i = 0
    lista_convertido = []
    lista_restos = []
    lista_restos.append(valor_fracionario)

    while continuar:
        res = lista_restos[i] * base
        lista_restos.append(float("0." + str(res).split(".")[1]))
        lista_convertido.append(int(res))

        # verificar se o valor atual já está na lista de restos, sendo assim, é uma dízima
        for j in range(len(lista_restos) - 1):
            if lista_restos[j - 1] == lista_restos[i]:
                continuar = False

        # limitar a precisão do resultado
        if len(lista_restos) > 4:
            continuar = False

        i += 1

    restos_string_float = str()
    for i in lista_convertido:
        restos_string_float += hexa[i]

    resultado = f"{restos_string_int}.{restos_string_float}"

    return resultado
