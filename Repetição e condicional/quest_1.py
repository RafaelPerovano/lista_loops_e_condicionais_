sair = False
while sair == False:
    q = int(input('Digite quantas notas são para o calculo da media: '))
    numero = []
    n = 0
    soma = 0 

    for i in range(q):
        c = i
        n = float(input('Digite o valor da nota: '))
        numero.append(n)
        soma = soma + n

    media = soma/q
    print('O valor da sua média é', media)
    
    parar = str(input('Se deseja parar de calcular a media digite "sair". '))
    if parar == 'sair':
        sair = True
