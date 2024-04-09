
lista_cliente = input('Informe as frutas desejadas (separadas por ";"): ')

lista_frutas = lista_cliente.replace(' ', '').split(";")

print(f'Primeiro item é: {lista_frutas[0]}')
print(f'Último item é: {lista_frutas.pop()}')
