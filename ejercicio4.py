def factorial (n):
    if n ==0:
        return 1
    else:
        return n * factorial (n - 1)
    
numero = 9
resultado = factorial(numero)
print(f"el factorial de {numero} es {resultado}")