musica = [("submarino amarillo", "los beatles", 9),
          ("imagine", "john lenon", 8),
          ("let it be", "los beatles", 7),
          ("bohemian rhapsody", "queen", 8),
          ("highway to the stars", "deep purple", 9)]

def buscar_cancion (nombre):
    for cancion in musica:
        if cancion[0] == nombre:
            return cancion
    return None

def busca_por_artista (artista):
    canciones_artista =[]
    for cancion in musica:
        if cancion [1] == artista:
            canciones_artista.append (cancion)
    return canciones_artista

busqueda = input ("ingrese nombre de cancion o del artista:").lower()
resultado_cancion = buscar_cancion(busqueda)
resultado_artista = busca_por_artista (busqueda)

if resultado_cancion:
    print (f"Cancion encontrada: {resultado_cancion}")
elif resultado_artista:
    print(f"canciones del artista {busqueda}:")
    for cancion in resultado_artista:
        print(f"Artista encontrado: {cancion}")
else:
    print ("No hay coincidencias")
