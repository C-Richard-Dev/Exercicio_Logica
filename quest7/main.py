alcool = 0
gasolina = 0
diesel = 0

while True:
    voto = int(input(
        f'\nInforme o código do combustível:\n'
        f'1. Álcool ({alcool})\n'
        f'2. Gasolina ({gasolina})\n'
        f'3. Diesel ({diesel})\n'
        f'4. Finalizar\n'
        'Digite o código: '
    ))

    if voto == 4:
        print(
            '\nMUITO OBRIGADO\n',
            f'Álcool - {alcool} votos\n'
            f'Gasolina - {gasolina} votos\n'
            f'Diesel - {diesel} votos\n'
            )
        break
    elif voto == 1:
        alcool += 1
    elif voto == 2:
        gasolina += 1
    elif voto == 3:
        diesel += 1
    else:
        print('Código inválido. Tente novamente.')
