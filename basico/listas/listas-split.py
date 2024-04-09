frutas_usuario = input('Digite os nomes das frutas separados por virgulas: ')

frutas_lista = frutas_usuario.replace(' ', '').split(',')

print(frutas_lista)
