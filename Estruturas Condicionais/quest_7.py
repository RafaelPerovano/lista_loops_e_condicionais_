x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

if x > 0 and y > 0:
    print('Esta no quadrante 1.')
elif x < 0 and y > 0:
    print('Esta no quadrante 2.')
elif x < 0 and y < 0:
    print('Esta no terceiro quadrante.')
else:
    print('Esta no quarto quadrante.')