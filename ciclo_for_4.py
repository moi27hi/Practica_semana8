# Llenando listas con un ciclo for


clientes_cafe = []
pedidos = []
print('***Bienvenido acafetería Express. Por favor, ingrese su nombre y pedido.***')
for i in range(1):
    cliente = input ('Ingrese su nombre: ')
    pedido = input ('Ingrese su pedido: ')
    clientes_cafe.append(cliente)
    pedidos.append(pedido)

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
    


for i in range (len(clientes_cafe)):
        cliente = clientes_cafe[i]
        pedido = pedidos[i]
        print(f'{cliente} su pedido es {pedido}. El precio es ${precio}.')
