import random

for i in range(0,1):
    nove_digitos = ''
    contador_regressivo_01 = 10
    calculo_01 = 0

    for i in range(0,9):
        nove_digitos += str(random.randint(0,9))

    for digito_01 in nove_digitos:
        calculo_01 += (int(digito_01) * contador_regressivo_01)
        contador_regressivo_01 -= 1

    primeiro_digito = (calculo_01 * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


    dez_digitos = nove_digitos + str(primeiro_digito)
    contador_regressivo_02 = 11
    calculo_02 = 0

    for digito_02 in dez_digitos:
        calculo_02 += int(digito_02) * contador_regressivo_02
        contador_regressivo_02 -= 1

    segundo_digito = (calculo_02 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0


    cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado)
