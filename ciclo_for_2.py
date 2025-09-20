
# Ciclo for para cadenas de texto.

Cadena = input("Ingrese una palabra: ").lower()
for caracter in Cadena:
    if caracter in "aeo":
        print(caracter)



lista = ['Axell','Piogram','Youtube','Python']

for cadena in lista:
    print('--- ' +cadena+ '---')

    for caracter in cadena:
        mini = caracter.lower()
        if mini in 'aeoáéó':
            print(mini)

print('Fin del programa')

    