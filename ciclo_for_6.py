estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
notas = [45, 92, 38, 90, 88]

for z in range(len(estudiantes)):
    estudiante = estudiantes[z]
    nota = notas[z]
    
    if nota >= 60 :
        print(f'Felicidades {estudiante}, has aprobado el curso.\n')
    elif nota <=59:
        print(f'Lo siento {estudiante}, has reprobado el curso.\n')
    else:
        print('Error en la nota.\n')

