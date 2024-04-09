while True:
    fruta = input('Informe o nome da fruta secreta: ')
    if fruta.replace(' ', '').lower() == 'abacate':
        break
    else:
        print(f'Errou!! {fruta} não é a fruta secreta.')

print('Parabéns, você acertou a fruta.')
