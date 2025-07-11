from formulario import Calculadora

def mostrar_menu():
    calc = Calculadora()

    while True:
        print("\n MENÚ DE OPCIONES ")
        print("1. Agregar par de números")
        print("2. Insertar par de números en una posición")
        print("3. Eliminar por posición")
        print("4. Remover par específico")
        print("5. Buscar índice de un par")
        print("6. Ver lista")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calc.almacenar_numero()
        elif opcion == "2":
            calc.insertar_valor()
        elif opcion == "3":
            calc.eliminar_valor()
        elif opcion == "4":
            calc.remover_valor()
        elif opcion == "5":
            calc.index_valor()
        elif opcion == "6":
            calc.ver_numero()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
