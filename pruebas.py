notas = []

while True:
    nota = input("Ingrese una calificacion (o 'salir' para terminar): ")

    if nota.lower() =='salir':
        break
    else:
        notas.append(float(nota))

promedio = sum(notas) / len(notas)
print("el primedio de notas es:", promedio)
