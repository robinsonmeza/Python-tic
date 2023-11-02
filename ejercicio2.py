import math

def area_circulo(radio):
    area = math.pi * (radio **2)
    return area
radio = 5
resultado = area_circulo (radio)
print(f"el area del circulo con dario {radio} es: {resultado}")