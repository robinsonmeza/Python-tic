# Solicita al usuario ingresar el peso en kilogramos, la altura en metros y la edad en años
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad en años: "))

# Calcula el Índice de Grasa Corporal (IGC) utilizando la fórmula de Dubois
IGC = (1.20 * peso) + (0.23 * (altura ** 2)) - (10.8 * edad) - 5.4

# Interpreta el IGC según la escala de clasificación
if IGC < 18.5:
    resultado = "Bajo peso o insuficiencia ponderal"
elif 18.5 <= IGC < 25.0:
    resultado = "Rango saludable o peso normal"
elif 25.0 <= IGC < 30.0:
    resultado = "Sobrepeso"
elif 30.0 <= IGC < 35.0:
    resultado = "Obesidad de grado 1 (leve)"
elif 35.0 <= IGC < 40.0:
    resultado = "Obesidad de grado 2 (moderada)"
else:
    resultado = "Obesidad de grado 3 (grave)"

# Imprime el resultado y la interpretación
print(f"Su Índice de Grasa Corporal es: {IGC:.2f}")
print(f"Su IGC se cataloga como: {resultado}")
