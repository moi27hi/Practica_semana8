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