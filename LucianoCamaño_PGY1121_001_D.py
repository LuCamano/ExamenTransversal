from os import system
from tabulate import tabulate #usando "pip install tabulate" instalo la libreria para poder hacer tablas más ordenadas
import numpy as np
system('cls')
Asientos =[[1,2,3,4,5,6,7,8,9,10],
        [11,12,13,14,15,16,17,18,19,20],
        [21,22,23,24,25,26,27,28,29,30],
        [31,32,33,34,35,36,37,38,39,40],
        [41,42,43,44,45,46,47,48,49,50],
        [51,52,53,54,55,56,57,58,59,60],
        [61,62,63,64,65,66,67,68,69,70],
        [71,72,73,74,75,76,77,78,79,80],
        [81,82,83,84,85,86,87,88,89,90],
        [91,92,93,94,95,96,97,98,99,100]]
reservados = []
run = []
nombreAsistente = []

#Definir funciones

def ComprarEntrada():
    while True:
        try:
            cantidad = int(input('Platinum $120.000. (Asientos del 1 al 20)\nGold $80.000. (Asientos del 21 al 50)\nSilver $50.000. (Asientos del 51 al 100)\nIngrese cantidad de entradas a comprar (max. 3): '))
            if cantidad >= 1 and cantidad <= 3:
                print(tabulate(Asientos, headers='Escenario ', tablefmt='grid'))
                print('Elija su(s) asiento(s)')
                EleccionAsiento(cantidad)
                break
        except:
            print('Entrada no válida')

def EleccionAsiento(cuantos):
    for i in range(cuantos):
        elegido = False
        while not elegido:
            try:
                asiento = int(input('Ingrese el asiento que desea elegir: '))
                if asiento <= 20:
                    valor = 120000
                    tipo = 'Platinum'
                elif asiento > 20 and asiento <=50:
                    valor = 80000
                    tipo = 'Gold'
                elif asiento > 50 and asiento <= 100:
                    valor = 50000
                    tipo = 'Silver'
                for fila in Asientos:
                    for elemento in fila:
                        if elemento == asiento:
                            pos = fila.index(elemento)
                            nroFila = Asientos.index(fila)
                            reservados.append(elemento)
                            while True:
                                try:
                                    runAsiento = int(input('Ingrese el run del ocupante sin puntos, guión ni digito verificador: '))
                                    while True:
                                        try:
                                            nombre = str(input('Ingrese nombre del ocupante: '))
                                            nombre = nombre.capitalize()
                                            nombreAsistente.append(nombre)
                                            break
                                        except:
                                            print('Nombre no válido')
                                    run.append(runAsiento)
                                    break
                                except:
                                    print('Entrada no válida')
                            print(f'Asiento {tipo} {asiento} reservado correctamente por un valor de ${valor} al run: {runAsiento}')
                            elegido = True
                if not elegido:
                    print('El asiento no esta disponible')
            except:
                print('Entrada no válida')
        Asientos[nroFila][pos] = 'X'

def ListadoAsistentes():
    listado = [['Asiento', 'Run', 'Nombre']]
    for i in range(len(run)):
        agregar = [reservados[i], run[i], nombreAsistente[i]]
        listado.append(agregar)
    print(tabulate(listado, headers='firstrow', tablefmt='grid'))

def GananciasTotale():
    cPlatinum = 0
    cGold = 0
    cSilver = 0
    totalPlatinum = 0
    totalGold = 0
    totalSilver = 0
    for nroAsiento in reservados:
        if nroAsiento > 0 and nroAsiento <= 20:
            cPlatinum += 1
        elif nroAsiento >= 21 and nroAsiento <= 50:
            cGold += 1
        elif nroAsiento >= 51 and nroAsiento <= 100:
            cSilver += 1
    totalPlatinum = cPlatinum * 120000
    totalGold = cGold * 80000
    totalSilver = cSilver * 50000
    total = totalPlatinum + totalGold + totalSilver

    lista = [['Tipo Entrada', 'Cantidad', 'Total'],['Platinum', cPlatinum, totalPlatinum],['Gold', cGold, totalGold],['Silver', cSilver, totalSilver]]
    print(tabulate(lista, headers='firsrow', tablefmt='grid'))


#Main

while True:
    try:
        opt = int(input('   Creativos.cl\nElija una opción:\n1. Comprar entradas\n2. Mostrar ubicaciones disponibles\n3. Ver listado de asistentes\n4. Mostrar ganancias totales\n5. Salir\n> '))
        if opt == 5:
            break
        elif opt == 1:
            ComprarEntrada()
        elif opt == 2:
            print(tabulate(Asientos, headers='Escenario ', tablefmt='grid'))
        elif opt == 3:
            ListadoAsistentes()
        elif opt == 4:
            GananciasTotale()
        else:
            print('Debe elegir una de las opciones listadas.')
    except:
        print('Opción no válida')
