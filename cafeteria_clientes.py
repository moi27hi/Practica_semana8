# Llenando listas con un ciclo for

clientes_cafe = []
pedidos = []
visitas = {}  # Diccionario para contar las visitas por cliente
print('***Bienvenido a Cafetería Express. Por favor, ingrese su nombre y pedido.***')

# Cambia el rango para permitir múltiples pedidos o usa un bucle while para entrada dinámica
while True:
    cliente = input('Ingrese su nombre (o "salir" para terminar): ')
    if cliente.lower() == 'salir':
        break
    
    pedido = input('Ingrese su pedido: ')
    clientes_cafe.append(cliente)
    pedidos.append(pedido)

    # Registrar la visita del cliente
    if cliente in visitas:
        visitas[cliente] += 1
    else:
        visitas[cliente] = 1

    # Asignar precio según el pedido
    if pedido == 'Latte':
        precio = 2.50
    elif pedido == 'Americano':
        precio = 1.50
    elif pedido == 'Capuchino':
        precio = 3.00
    elif pedido == 'Espresso':
        precio = 2.00
    elif pedido == 'Mocha':
        precio = 3.50
    elif pedido == 'Machiato':
        precio = 2.50
    elif pedido == 'Leche':
        precio = 1.00
    else:
        print('Lo siento, no tenemos ese pedido.')
        precio = 0.00  # Precio por defecto para pedidos inválidos

# Mostrar los pedidos registrados
for i in range(len(clientes_cafe)):
    cliente = clientes_cafe[i]
    pedido = pedidos[i]
    print(f'{cliente} su pedido es {pedido}. El precio es ${precio:.2f}.')

# Mostrar el número de visitas por cliente
print("\n*** Registro de visitas ***")
for cliente, num_visitas in visitas.items():
    print(f'{cliente} ha visitado la cafetería {num_visitas} vez/veces.')