notas = []  # Inicia una lista vacía llamada "notas" para almacenar calificaciones.

while True:  # Inicia un bucle que se ejecutará indefinidamente (hasta que se rompa con "salir" explícitamente).
    nota = input("Ingrese una calificación (o 'salir' para terminar): ")  # Solicita al usuario ingresar una calificación o 'salir' para terminar.

    if nota.lower() == 'salir':  # sí la "nota" es igual a 'salir' (sin importar mayúsculas/minúsculas).
        break  # Si se ingresó 'salir', rompe el bucle y continúa con el código siguiente.
    else:
        notas.append(float(nota))  # Convierte la entrada del usuario en un número de punto flotante y lo agrega a la lista "notas".

promedio = sum(notas) / len(notas)  # Calcula el promedio de las calificaciones sumando todas las calificaciones y dividiendo por la cantidad de calificaciones.
print("El promedio de notas es:", promedio)  # Imprime el resultado del promedio de calificaciones.
