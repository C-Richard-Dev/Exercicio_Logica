# Ler Hora inicial e final de um jogo

hora_inicio = int(input('Hora início: '))
hora_final = int(input('Hora fim: '))


# calcular duração do jogo (min 1h, max 24h)

if hora_inicio < hora_final:
    print(hora_final - hora_inicio)
    

elif hora_inicio > hora_final:
    calc = 24 - hora_inicio
    result = calc + hora_final
    print(result)

else:
    result = 24
    print(result) 


    
