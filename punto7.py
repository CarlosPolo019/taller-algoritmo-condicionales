valorMarca = int(input('El producto es marca NOSY ? Responda con un 1 si la respuesta es POSITIVA y con un 0 si la respuesta es NEGATIVA: '))

valorProducto = float(input('Digite el valor del producto: '))

if valorProducto > 0:
    if valorMarca == 1:
        valorCompra =  valorProducto * 1.16
        descuento = (0.10 * valorProducto)
        if valorProducto >= 2000:       
           total = valorCompra - descuento - (valorCompra*0.05)
        else:
            total = valorCompra - descuento
        print(f'Se le aplicara un descuento del: 10%')
        print(f'Valor del producto sin Iva: {valorProducto}')
        print(f'Valor del producto con Iva: {valorCompra}')
        print(f'Valor de la compra con descuento de : {total}')
    elif valorMarca == 0:
        valorCompra =  valorProducto * 1.16
        descuento = (0.10 * valorProducto)
        total = valorCompra - descuento
        print(f'Se le aplicara un descuento del: 10%')
        print(f'Valor del producto sin Iva: {valorProducto}')
        print(f'Valor del producto con Iva: {valorCompra}')
        print(f'Valor de la compra con descuento: {total}')
    else:
        print(f'Respuesta de la marca incorrecta')
else:
    print(f'El valor ingresado debe ser mayor a 0')
