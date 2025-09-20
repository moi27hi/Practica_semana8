# Ejercicio 2

acum = 0
cuantos = int(input('Cuantos numeros desea digitar: '))
ciclo = 0
while ciclo < cuantos:
    numero = int(input('Ingrese un numero: '))
    acum += numero
    ciclo += 1
print(f'El total de la suma es: {acum}')



