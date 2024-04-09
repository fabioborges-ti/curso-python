# **************************************************
# RESPOSTA COM USO DE LISTAS
# **************************************************

# paises = ['brasil', 'china', 'espanha', 'franca', 'argentina']
# capitais = ['brasilia', 'pequim', 'madrid', 'paris', 'buenos aires']

# continua = True

# while continua:
#     pais_informado = input('Informe o pais desejado: ')
#     if pais_informado in paises:
#         for i, pais in enumerate(paises):
#             if pais_informado == pais:
#                 capital = capitais[i]
#                 print(f'A capital do pais selecionado é {capital.upper()}.')
#                 continua = False
#                 break
#     else:
#         print('Pais nao encontrado')

# print('fim  do programa')

# **************************************************
# RESPOSTA COM USO DE DICIONARIOS
# **************************************************

capitais = {
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

pais_usuario = input('Digite o nome do pais: ')

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}.')
else:
    print('desculpe, naotemos a informacao desse pais.')

print('fim do programa')
