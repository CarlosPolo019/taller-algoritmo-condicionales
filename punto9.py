numUno = float(input('Digite un numero: '))

numDos = float(input('Digite un numero: '))


if numUno == numUno:
    total = numUno * numDos
    print(f'Los numeros son iguales')
elif numUno > numDos:
    total = numUno - numDos
    print(f'El primer numero es mayor al segundo')
else: 
    total = numUno + numDos
    print(f'El primer numero es menor que el segundo')

print(f'Resultado: {total}')
