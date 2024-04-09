
numero = int(input('Informe um número [0 encerra]: '))

while numero != 0:
    if numero == 10:
        print('O numero que voce informou é 10')
    elif numero < 10:
        print('O numero que voce informou é menor que 10')
    else:
        print('O numero que voce informou é maior que 10')

    numero = int(input('Informe um número [0 encerra]: '))
