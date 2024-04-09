estoque = ['bmw x6', 'bmw i5', 'bmw i8']

opcao = input('Informe o carro desejado (ou escreva sair): ').lower()

while opcao.lower() != 'sair':
    if opcao.lower() in estoque:
        print('Carro disponível para compra.')
    else:
        print('Desculpe, este modelo não está disponível.')

    opcao = input('Informe o carro desejado (ou escreva sair): ').lower()

print('saiu do sistema.')
