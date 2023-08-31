lado1 = float(input('Digite o primeiro lado de um triangulo. '))
lado2 = float(input('Digite o segundo lado de um triangulo. '))
lado3 = float(input('Digite o terceiro lado de um triangulo. '))

if lado1 == lado2 and lado2 == lado3:
    print('Seu triangulo é equilatero.')
elif lado1 != lado2 and lado2 != lado3:
    print('Seu triangulo é isósceles.')
else:
    print('Seu triagulo é escaleno.')