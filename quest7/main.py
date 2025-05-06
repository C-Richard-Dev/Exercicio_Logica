alcool = 0
gasolina = 0
diesel = 0

while True:
    voto = input(
        'Informe o código do combustível:\n' \
        '1.Álcool(',alcool,')\n' \
        '2.Gasolina(',gasolina,')\n' \
        '3.Diesel(',diesel,')\n' \
        '4.Finalizar'\
        '\n '
    )

    if voto == 4:
        print('MUITO OBRIGADO')
        break
    elif voto == 1:
        alcool + 1
    elif voto == 2:
        gasolina + 1 
    elif voto == 3:
        diesel + 1
