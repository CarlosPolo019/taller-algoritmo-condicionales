numUno = float(input('Digite un numero: '))

numDos = float(input('Digite un numero: '))

if numUno == numDos: 
    print(f'Los numeros no pueden ser iguales')
else:

    numTercero = float(input('Digite un numero: '))
    if numUno == numTercero:
        print(f'Ingreso este mismo numero en la primera opcion')
    elif numDos == numTercero:
        print(f'Ingreso este mismo numero en la segunda opcion')
    else: 
        if numUno > numDos and numUno > numTercero:
            print(f'El primer numero ingresado es el mayor: {numUno}')
        elif numDos > numUno and numDos > numTercero:
            print(f'El segundo numero ingresado es el mayor: {numDos}')
        else:
            print(f'El tercer numero ingresado es el mayor: {numTercero}')

