# Bucle for por indices.

frutas = ['Mora','manzana', 'banana', 'pera', 'naranja']

for i in range(len(frutas)):
    fruta = frutas[i]
    print(i+1, "._", fruta)




comida_favorita = ['Pizza', 'Hamburguesa', 'Helado', 'jiao Zi', 'Tacos']

for i in range(len(comida_favorita)):
    comida = comida_favorita[i]
    print(f'{i+1}. Me gusta el/la {comida}.') 


materias = ['Estadistica','Programacion 3','Inglés','Base de datos','Electronica']

print('Este ciclo tengo las materias siguientes:\n')

for i in range(len(materias)):
    materia = materias[i]
    print(f'{i+1}. {materia}.')



frutas = ['Mora','manzana', 'banana', 'pera', 'naranja']

precioxlb = [0.50,1.00,1.55,1,20,2.00]

print('Lista de frutas con precio menor a 1.50')

for i in range(len(frutas)):
    fruta = frutas[i]
    precio = precioxlb[i]
    if precio < 1.50:
        print(fruta)




clientes_cafe = ['Axell','Zarinna','Luis','Joel','Kevin','Esteban']
pedidos = ['Café','Latte','Capuchino','Espresso','Mocha','Latte']
precios = [1.00,2.50,3.00,1.50,3.50,2.50]

for i in range(len(clientes_cafe)):
    cliente = clientes_cafe[i]
    pedido = pedidos[i]
    precio = precios[i]

    if pedido == 'Latte':
        print(f'{cliente} pidió un {pedido} con un precio de ${precio}.')

    if precio > 2.00:
        print(f'{cliente} pagó ${precio} por su {pedido}.')











#frutas = ['Mora','Fresa','Mora','Pina','Uva']
#cantidad = [5, 10,3,,5,10]
#clientes = ['Axell','Zarinna','Luis','Joel','Kevin']

# Imprimir por pantalla todas las personas que compraron Mora y la cantidad.

