nombres = []
edad = []


for i in range(1):
    nombre = input('Ingrese un nombre: ')
    ed = int(input('Ingrese su edad: '))
    nombres.append(nombre)
    edad.append(ed)
    nombre = nombres[i]
    ed = edad[i]
    print(f'Hola {nombre}, tienes {ed} años.')


print (nombres)
print (edad)
   

