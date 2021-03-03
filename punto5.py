valorCarro = float(input('Digite el valor del carro: '))
valorTerreno = float(input('Digite el valor del terreo: '))

incrementoTerreno = 0.10 * valorTerreno * 3
desvaluacionCarro = 0.10 * valorCarro * 3
print(f'Valor Terreno {desvaluacionCarro}')
if (desvaluacionCarro < (incrementoTerreno*0.50)):
    print(f'Calculos Finalizados')
    print(f'Usted debe comprar el carro')
else:
    print(f'Calculos Finalizados')
    print(f'Usted debe comprar el terreno')
