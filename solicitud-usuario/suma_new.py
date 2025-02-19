def suma():
    try:
        a = int(input("Dame un número: "))
        b = int(input("Dame otro número: "))
        resultado = a + b
        print(f"La suma de {a} y {b} es: {resultado}")
        print(f"La división de {a} y {b} es: {a/b}")
    except ValueError:
        print("Error: Debes ingresar solo números.")

if __name__ == "__main__":
    suma()
