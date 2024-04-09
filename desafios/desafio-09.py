# desafio remover maça e o último item da lista

frutas = ['maça', 'morango', 'manga', 'uva', 'abacaxi']

if 'manga' in frutas:
    frutas.remove('manga')

ultima_fruta = frutas[len(frutas) - 1]

# frutas.remove(ultima_fruta)       # jeito tradicional
# del frutas[-1]                    # recurso rápido

print(frutas)
