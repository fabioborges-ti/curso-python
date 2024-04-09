idade = int(input('Informe sua idade [0 encerra]: '))

while idade != 0:
    if idade <= 13:
        print('Você é uma criança.')
    elif 13 < idade <= 19:
        print('Você é um adolescente.')
    else:
        print('Você já é um adulto.')

    idade = int(input('Informe sua idade [0 encerra]: '))
