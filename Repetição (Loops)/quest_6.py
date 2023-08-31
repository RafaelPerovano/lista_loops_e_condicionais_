q = int(input('Digite a quantidade de numeros que deseja ver na sequencia de fibonacci: '))
n1 = 0 
n2 = 1
for i in range(0, q+1):
    resp = n1 + n2
    print(n1)
    n1 = n2
    n2 = resp   