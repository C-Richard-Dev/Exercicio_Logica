l1 = list(range(0,25))
l2 = list(range(25,50))
l3 = list(range(50,75))
l4 = list(range(75,100))

number = int(input('Digite um valor: '))

if number in l1:
    print('O número esta no intervalo (0,25)')
elif number in l2: 
    print('O número esta no intervalo (25,50)')
elif number in l3: 
    print('O número esta no intervalo (50,75)')
elif number in l4: 
    print('O número esta no intervalo (75,100)')
else:
    print('Fora de intervalo')


