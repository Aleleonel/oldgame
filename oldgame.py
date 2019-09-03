tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
op = 's'
print('-='*11)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{tabuleiro[i][j]:^5}]', end='')
    print()
print('-='*11)
while op != 'n':
    escolha = int(input('Digite 1 para X ou 2 para O: '))
    jogada = int(input('Digite o numero da sua jogada: '))
    if escolha == 1:
        for l in range(0, 3):
            for c in range(len(tabuleiro)):
                if tabuleiro[l][c] == jogada:
                    tabuleiro[l][c] = 'x'
    else:
        for l in range(0, 3):
            for c in range(len(tabuleiro)):
                if tabuleiro[l][c] == jogada:
                    tabuleiro[l][c] = 'O'

    print('-='*11)
    for i in range(0, 3):
        for j in range(0, 3):
            print(f'[{tabuleiro[i][j]:^5}]', end='')
        print()
    print('-='*11)
    op = input('Deseja contiuar: [s]/[n]: ')