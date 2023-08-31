numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite um segundo numero: '))
numero3 = float(input('Digite um terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1, 'é o maior')
elif numero2 > numero1 and numero2 > numero3:
    print(numero2, 'é o maior')
else:
    print(numero3, 'é o maior')