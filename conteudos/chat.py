import os

mensagens = []

nome = input('Nome: ')

while True:
    os.system('cls')  # clear

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print('__________________')

    texto = input('mensagem: ')
    if texto == 'fim':
        break  # quebra o loop

    mensagens.append({
        'nome': nome,
        'texto': texto
    })
