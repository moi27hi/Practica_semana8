# Menu

opcion = " "

while opcion != 5:
    print(''' Bienvenido a su conversor de unidadades
          1. Convertir de metros a centimetros
          2. Convertir de centimetros a metros
          3. Convertir de metros a pulgadas
          4. Convertir de pulgadas a metros
          5. Salir''')
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        metros = float(input('Ingrese la cantidad en metros: '))
        centimetros = metros * 100
        print(f'{metros} metros son {round(centimetros, 2)} centimetros')
    elif opcion == 2:
        centimetros = float(input('Ingrese la cantidad en centimetros: '))
        metros = centimetros / 100
        print(f'{centimetros} centimetros son {round(metros, 2)} metros') 
    elif opcion == 3:
        metros = float(input('Ingrese la cantidad en metros: '))
        pulgadas = metros * 39.37
        print(f'{metros} metros son {round(pulgadas, 2)} pulgadas')
    elif opcion == 4:
        pulgadas = float(input('Ingrese la cantidad en pulgadas: '))
        metros = pulgadas / 39.37
        print(f'{pulgadas} pulgadas son {round(metros, 2)} metros')
    elif opcion == 5:
        print('Gracias por usar el conversor. ¡Hasta luego!') 