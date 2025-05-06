valor = int(input('Digite um numero inteiro entre 1 e 1000: '))

if valor >1000 or valor<0:
    valor = int(input('O numero deve estar entre 1 e 1000: '))

impares = []

for i in range(1, valor+1):
    if i % 2 != 0:
        impares.append(i)

print(impares)