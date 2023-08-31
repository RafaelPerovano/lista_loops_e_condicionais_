q = int(input('Digite a quantidade de numeros que deseja verificar: '))
numeros = []
n_maior = 0
for i in range(0, q):
    numeros.append(float(input('Digite numeros: ')))
i = 0

for i in range(0, q):
    if numeros[i] > n_maior:
        n_maior = numeros[i]
        
print('O numero maior é' , n_maior)