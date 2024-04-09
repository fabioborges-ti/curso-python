
cidades = ['Rio de Janeiro', 'Sao Paulo', 'Curitiba', 'Goiania', 'Brasilia']
valores = [10, 20, 30, 40, 50]

lista_final = list()

for x in cidades:
    i = cidades.index(x)
    for y in valores:
        if valores.index(y) == i:
            item = [cidades[i], valores[i]]
            lista_final.append(item)

print(lista_final)
