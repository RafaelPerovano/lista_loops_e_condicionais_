ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} nao é um ano bissexto.'.format(ano))