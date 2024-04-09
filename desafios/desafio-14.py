print('Loop ate o número 5:')
print('*******************************************')

for x in range(1, 10):
    print(x)
    if (x == 5):
        break

print('\n')
print('Loop para pular o número 5:')
print('*******************************************')

for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)

print('\n')
print('Loop para pular o número 5: (com while)')
print('*******************************************')

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
