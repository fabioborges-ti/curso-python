def potencia(base, potencia=2):
    return base ** potencia


base = input('Favor, informe o numero base: ')
pote = input('Favor, informe a potencia: ')

resultado = 0

if pote:
    resultado = potencia(int(base), int(pote))
else:
    resultado = potencia(int(base))

print(f'Resultado = {resultado}')
