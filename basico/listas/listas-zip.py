produtos = ['arroz', 'melancia', 'laranja', 'banana']
valores = [10, 20, 30, 40]

lista = list()

for i in range(len(produtos)):
    for v in range(len(valores)):
        if i == v:
            produto = [produtos[i], valores[v]]
            lista.append(produto)

# funcao zip
# relaciona cada index de uma lista ao index da segunda lista
# lista = list(zip(produtos, valores))

print(lista)
