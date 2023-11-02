precio = 50
denominaciones = [25, 10, 5]
ingresado = 0
adeudado = precio

while adeudado > 0:
    moneda = int(input("Inserte una moneda (5, 10 o 25 centavos):"))
    if moneda in denominaciones:
            ingresado += moneda
            adeudado -= moneda
            print("monto adeudado: {} centavos".format(adeudado))
    else:
        print("Moneda no aceptada. Inserte una moneda (5, 10 o 25 centavos")
    
if ingresado > precio:
    cambio = ingresado - precio
    print("cambio: {} centavos".format(adeudado))