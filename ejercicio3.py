def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    return celsius

temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados celsius equivalen a {temperatura_fahrenheit:.2f} grados fahrenheit")

temperatura_fahrenheit = 66
temperatura_celsius = fahrenheit_a_celsius (temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados fahrenheit equivalen a {temperatura_celsius:.2f} grados celsius")