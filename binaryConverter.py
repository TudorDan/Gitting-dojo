def zecimal_spre_binar(n):
    x = n
    i = 1
    solutie = 0
    while x > 0:
        restul = x % 2
        solutie = solutie + (i * restul)
        i *= 10
        x = x // 2
    print(f"Numarul zecimal '{n}' este: {solutie} in baza 2.")


def binar_catre_zecimal(n):
    x = n
    i = 1
    solutie = 0
    while x > 0:
        restul = x % 10
        solutie = solutie + (i * restul)
        i *= 2
        x = x // 10
    # Alternative solution
    # x = str(n)
    # lungime_n = len(x)
    # solutie = 0
    # for i in range(1, lungime_n + 1):
    #     solutie = solutie + int(x[i - 1]) * 2 ** (lungime_n - i)
    print(f"Numarul binar '{n}' este: {solutie} in baza 10.")


numar = input('Introduceti numarul si baza in care se afla:')

lista = numar.split()

if lista[1] == '2':
    binar_catre_zecimal(int(lista[0]))
else:
    zecimal_spre_binar(int(lista[0]))


# zecimal_spre_binar(275)
# zecimal_spre_binar(256)
# zecimal_spre_binar(1975)
# binar_catre_zecimal(1011)
# binar_catre_zecimal(111)
# binar_catre_zecimal(11110110111)
