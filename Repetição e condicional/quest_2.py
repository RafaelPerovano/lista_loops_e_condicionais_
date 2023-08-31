sair = True

while sair:
    numero = []
    n_menor = 1000000
    n = float(input('Digite os valores para verificar qual numero é menor: '))
    numero.append(n)

    if n_menor > n:
        n_menor = n
    exit = input('Se quiser parar de executar o codigo digite [sair] ')

    if exit == "sair":
        sair = False

print('Seu menor numero é {}.'.format(n_menor))
    