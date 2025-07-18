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
        print("6. Contar ocurrencias de un par")
        print("7. Ordenar lista")
        print("8. Invertir lista")
        print("9. Ver lista de números")
        print("10. tuplas")
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
            calc.count_valor()
        elif opcion == "7":
            calc.sort_valor()
        elif opcion == "8":
            calc.reverse_valor()
        elif opcion == "9":
            calc.ver_numero()
        elif opcion == "10":
            while True:
                print("1. Ver tupla de pares")
                print("2. Agregar número par")
                print("3. Eliminar número par")
                print("4. Modificar número par")
                print("5. Ver tupla de impares")
                print("6. Agregar número impar")
                print("7. Eliminar número impar")
                print("8. Modificar número impar")
                print("0. Volver al menú principal")

                sub_opcion = input("Seleccione una opción del submenú: ")

                if sub_opcion == "1":
                    print(calc.objlista.tupla_pares)
                elif sub_opcion == "2":
                    calc.agregar_a_tupla_pares()
                elif sub_opcion == "3":
                    calc.eliminar_de_tupla_pares()
                elif sub_opcion == "4":
                    calc.modificar_tupla_pares()
                elif sub_opcion == "5":
                    print(calc.objlista.tupla_impares)
                elif sub_opcion == "6":
                    calc.agregar_a_tupla_impares()
                elif sub_opcion == "7":
                    calc.eliminar_de_tupla_impares()
                elif sub_opcion == "8":
                    calc.modificar_tupla_impares()
                elif sub_opcion == "0":
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
                    print("Saliendo del programa.")
                    break
        if opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    mostrar_menu()
