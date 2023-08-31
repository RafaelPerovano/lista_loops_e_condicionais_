q = int(input('Digite a quantidade de numeros que deseja verificar: '))
numeros = []
cp = 0
ci =0

for i in range(0, q):
    numeros.append(float(input('Digite numeros: ')))

for c in range(0, q):
    if numeros[c] % 2 == 0:
        cp += 1
    else:
        ci += 1

print('existem {} numeros pares e {} impares nessa lista de numeros.'.format(cp, ci))