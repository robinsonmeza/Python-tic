def main():
    palabra = input("Ingrese una palabra: ")
    resultado = twtter(palabra)
    print("la palabra abreviada es: "+ ''.join(resultado))

def twtter(pal):
    pal = pal.lower()
    sal = []
    for z in range(len(pal)):
        if pal[z] not in ["a","e","i","o","u"]:
            sal.append(pal[z])
    return sal

if __name__ =="__main__":
    main()
