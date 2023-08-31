numero = int(input('Digite o valor que deseja ver a tabuada: '))
x = 1

while x <= numero:
    mult = numero * x
    print('{} x {} = {}'.format(numero, x , mult))
    x += 1