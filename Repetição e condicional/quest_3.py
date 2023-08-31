from random import randint
numero = float(input('Digite um numero para tentar adivinhar de 0 a 100: '))
n = randint(0, 100)
acertou = False

while acertou == False:
    if numero == n:
        print('PARABÉNS! VOCE ACERTOU!')
        break
    numero = float(input('Ops... Tente adivinhar o numero novamente:'))
    
