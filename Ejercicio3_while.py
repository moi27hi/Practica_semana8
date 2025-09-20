# Ejercicio 3

opcion = ""

while opcion != 3:
    print('''Bienvenido a tu calculadora
          1. Suma
          2. Resta
          3. Salir''')
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        suma = num1 + num2
        print(f'El resultado de la suma es: {suma}')
    elif opcion == 2:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        resta = num1 - num2
        print(f'El resultado de la resta es: {resta}')
    elif opcion == 3:
        print('Gracias por usar la calculadora. ¡Hasta luego!')
    else:
        print('Opcion no valida, por favor intente de nuevo.')
