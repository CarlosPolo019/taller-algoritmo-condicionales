diaUno = float(input('Digite el punto emitido en el dia 1: '))
diaUnoGanancia = float(input('Digite el valor de ganancias en el dia 1: '))

diaDos = float(input('Digite el punto emitido en el dia 2: '))
diaDosGanancia = float(input('Digite el valor de ganancias en el dia 2: '))

diaTres = float(input('Digite el punto emitido en el dia 3: '))
diaTresGanancia = float(input('Digite el valor de ganancias en el dia 3: '))

diaCuatro = float(input('Digite el punto emitido en el dia 4: '))
diaCuatroGanancia = float(input('Digite el valor de ganancias en el dia 4: '))

diaCinco = float(input('Digite el punto emitido en el dia 5: '))
diaCincoGanancia = float(input('Digite el valor de ganancias en el dia 5: '))

totalPuntos = diaUno + diaDos + diaTres + diaCuatro + diaCinco 
totalGanancias = diaUnoGanancia + diaDosGanancia + diaTresGanancia + diaCuatroGanancia + diaCincoGanancia 
promedio = totalPuntos/5

if promedio <= 170:
    print(f'Revison Finalizada')
    print(f'Puntos obtenidos: {totalPuntos}')
    print(f'Promedio de puntos: {promedio}')
    print(f'Ganancias generadas: {totalGanancias}')
    print(f'Usted cumple con las normativas y por lo tanto no recibira ninguna sancion o multa')
else:
    print(f'Revision Finalizada')
    print(f'Puntos obtenidos: {totalPuntos}')
    print(f'Promedio de puntos: {promedio}')
    print(f'Ganancias generadas: {totalGanancias}')
    print(f'Usted no cumple con las normativas y por lo tanto recibira una sancion de parar por una semana la produccion')
    print(f'Debera pagar una multa de : {totalGanancias*0.50}')
