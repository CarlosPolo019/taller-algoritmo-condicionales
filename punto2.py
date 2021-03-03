valorProducto = float(input('Digite el valor de la compra: '))
numeroAzar = int(input('Digite un numero: '))
if valorProducto > 0:
    if numeroAzar >= 74:
        descuento = (0.20 * valorProducto)
        total =  valorProducto - descuento
        print(f'Su compra aplica para un descuento del: 20%')
        print(f'El numero al azar ingresado fue: {numeroAzar}')
        print(f'Valor de la compra {valorProducto}')
        print(f'Valor del descuento 0{descuento}')
        print(f'Total compra con descuento {total}')
    else:
        descuento = (0.15 * valorProducto)
        total =  valorProducto - descuento
        print(f'Su compra aplica para un descuento del: 15%')
        print(f'El numero al azar ingresado fue: {numeroAzar}')
        print(f'Valor de la compra {valorProducto}')
        print(f'Valor del descuento {descuento}')
        print(f'Total compra con descuento {total}')
else:
    print(f'El valor de la compra debe ser mayor a 0')
