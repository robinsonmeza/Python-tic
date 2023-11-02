def main():
    menu = {
        "BAJA TACO": 4.00,
        "BURRITO": 7.50,
        "BOWL": 8.50,
        "NACHOS": 11.00,
        "QUESADILLA": 8.50,
        "SUPER BURRITO": 8.50,
        "SUPER QUESADILLA": 9.50,
        "TACO": 3.00,
        "TORTILLA SALAD": 8.00
    }
    Order_total = 0.0
    while True:
        try:
            item = input("ingrese su articulo al pedido: ")
        except EOFError:
            break
        item = item.upper()
        if item in menu:
            Order_total += menu[item]
            print(f"${Order_total:.2f}")
        elif item == "CONTROL-D":
            print(f"El total de su pedido es ${Order_total:.2f}")
            break
        else: 
            print("articulo invalido")

if __name__=="__main__":
    main()
