from base_para_decimal import base_para_decimal
from decimal_para_base import decimal_para_base


operacao = input(
    "Qual operação você deseja fazer? ('s' para soma; 'm' para multiplicação; 'c' para conversão simples) - "
)

if operacao == "c":
    n = input("Digite o valor para converter: ")
    b1, b2 = map(
        int,
        input(
            "Digite a base de origem e a base de destino separadas por espaço: "
        ).split(" "),
    )

    if b2 > 12:
        print("ERRO: Ainda não é possível realizar operações com bases maiores que 12. ")
        exit()

else:
    base = int(input("Em qual base você deseja realizar a operação? - "))
    n1 = input("Digite o primeiro valor da operação: ")
    n2 = input("Digite o segundo valor da operação: ")

    if base > 12:
        print("ERRO: Ainda não é possível realizar operações com bases maiores que 12. ")
        exit()

print("-" * 30)

match operacao:
    case "s":
        n1_decimal = base_para_decimal(n1, base)
        n2_decimal = base_para_decimal(n2, base)
        soma = n1_decimal + n2_decimal
        print(
            f"-> {n1} somado com {n2} na base {base} é igual a {decimal_para_base(str(soma), base)}"
        )
        print(f".O resultado em decimal é {round(soma, 4)}")
        print(f".O resultado em binário é {decimal_para_base(str(soma), 2)}")
        print(f".O resultado em octal é {decimal_para_base(str(soma), 8)}")
        print(f".O resultado em hexadecimal é {decimal_para_base(str(soma), 16)}")
    case "m":
        n1_decimal = base_para_decimal(n1, base)
        n2_decimal = base_para_decimal(n2, base)
        mult = n1_decimal * n2_decimal
        print(
            f"-> {n1} multiplicado por {n2} na base {base} é igual a {decimal_para_base(str(mult), base)}"
        )
        print(f".O resultado em decimal é {round(mult, 4)}")
        print(f".O resultado em binário é {decimal_para_base(str(mult), 2)}")
        print(f".O resultado em octal é {decimal_para_base(str(mult), 8)}")
        print(f".O resultado em hexadecimal é {decimal_para_base(str(mult), 16)}")
    case "c":
        print(
            f"O valor {n}({b1}) é igual a {decimal_para_base(str(base_para_decimal(n, b1)), b2)}({b2})"
        )
    case _:
        print("Operação inválida")
