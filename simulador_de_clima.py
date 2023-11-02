import random

def simular_condiciones_climaticas():
    temperatura_inicial = float(input("Ingrese la temperatura inicial (en °C): "))
    probabilidad_lluvia = float(input("Ingrese el porcentaje de probabilidad de lluvia: "))
    dias = int(input("Ingrese el número de días de predicción: "))

    temperatura = temperatura_inicial
    dias_lluvia = 0
    temperatura_maxima = temperatura
    temperatura_minima = temperatura

    for dia in range(1, dias + 1):
        print(f'Día {dia}: Temperatura: {temperatura}°C')

        # Verificar si llueve
        if random.random() * 100 < probabilidad_lluvia:
            print('Llueve')
            temperatura -= 1
            dias_lluvia += 1

        # Actualizar temperatura
        if random.random() * 100 < 10:
            temperatura += 2 if random.random() < 0.5 else -2

        # Verificar condiciones de temperatura
        if temperatura > 25:
            probabilidad_lluvia += 20
        elif temperatura < 5:
            probabilidad_lluvia -= 20

        # Mantener registro de la temperatura máxima y mínima
        temperatura_maxima = max(temperatura, temperatura_maxima)
        temperatura_minima = min(temperatura, temperatura_minima)

    print(f'Temperatura máxima: {temperatura_maxima}°C')
    print(f'Temperatura mínima: {temperatura_minima}°C')
    print(f'Días de lluvia: {dias_lluvia}')

# Ejemplo de uso
simular_condiciones_climaticas()

