import datetime

while True:
    nome = input("Digite seu nome completo: ")
    try:
        ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        if 1922 <= ano <= 2021:
            print(f"{nome} completou {datetime.datetime.now().year - ano} anos em 2022.")
            break
        else:
            print("Ano inválido. Digite um valor entre 1922 e 2021.")
    except ValueError:
        print("Digite um ano válido (apenas números).")