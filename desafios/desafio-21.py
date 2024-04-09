cidades = {'Rio de Janeiro', 'Sao Paulo', 'Salvador'}

contiua = False

while True:

    cidade_desejada = input('Informe o nome da cidade desejada: ')

    if cidade_desejada in cidades:
        print('A cidade esta na lista de cidades')
        condicao = False
        break
    else:
        print('A cidade NAO esta na lista de cidades')

print('fim do programa')
