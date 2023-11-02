peso = float(input("Introduzca su peso en Kg: ") )
altura = float(input("Introduzca su altura en metros: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    resultado = "Bajo peso"
elif IMC < 25:
    resultado = "Normal"
else:
    resultado = "Sobrepeso"

print(f"Total= {IMC:.1f} .Su IMC esta catalogado como {resultado}.")