# def fatorial(n: int):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         x = 1
#         for x in range(1, n):
#             result += result * x

#     return result

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input('Informe um numero: '))

resultado = fatorial(numero)

print(f'O fatorial do numero {numero} é {resultado}')
