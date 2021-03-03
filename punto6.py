numComputadoras = float(input('Digite la cantidad de computadoras a comprar: '))
if numComputadoras > 0:
    if numComputadoras < 5:
        valorCompra =  numComputadoras * 11000
        descuento = (0.10 * valorCompra)
        total = valorCompra - descuento
        print(f'Se le aplicara un descuento del: 10%')
        print(f'Valor de la compra sin descuento: {valorCompra}')
        print(f'Valor del descuento: {descuento}')
        print(f'Valor de la compra con descuento: {total}')
    elif (numComputadoras >= 5) and (numComputadoras < 10):
        valorCompra =  numComputadoras * 11000
        descuento = (0.20 * valorCompra)
        total = valorCompra - descuento
        print(f'Se le aplicara un descuento del: 20%')
        print(f'Valor de la compra sin descuento: {valorCompra}')
        print(f'Valor del descuento: {descuento}')
        print(f'Valor de la compra con descuento: {total}')
    else:
        valorCompra =  numComputadoras * 11000
        descuento = (0.40 * valorCompra)
        total = valorCompra - descuento
        print(f'Se le aplicara un descuento del: 40%')
        print(f'Valor de la compra sin descuento: {valorCompra}')
        print(f'Valor del descuento: {descuento}')
        print(f'Valor de la compra con descuento: {total}')
else:
    print(f'El valor ingresado debe ser mayor a 0')
