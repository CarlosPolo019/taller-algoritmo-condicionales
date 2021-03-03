valorFianza = float(input('Digite el monto de la fianza: '))
if valorFianza > 0:
    if valorFianza > 50000:
        cuota = (0.02 * valorFianza)
        print(f'Su fianza aplica para una cuota del: 2%')
        print(f'Valor de la fianza: {valorFianza}')
        print(f'El valor de la cuota a pagar es: {cuota}')
    else:
        cuota = (0.03 * valorFianza)
        print(f'Su fianza aplica para una cuota del: 3%')
        print(f'Valor de la fianza: {valorFianza}')
        print(f'El valor de la cuota a pagar es: {cuota}')
else:
    print(f'El valor de la fianza debe ser mayor a 0')
