divisores = []

num = int(input('Digite um número: '))

for i in range (1, num+1):
    if i % 2 == 0:
        divisores.append(i)

print(f'Os divisores de ',num,' são: ', divisores)
