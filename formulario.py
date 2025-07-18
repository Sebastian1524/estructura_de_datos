from lista_datos import Lista_numeros

class Calculadora:
    def __init__(self):
        self.objlista = Lista_numeros()
    
    def tupla_impares(self):
        return self.objlista.tuplea_impar()
    def tupla_datos(self):
        return self.objlista.tuplea_datos()
    
    def pedir_numeros(self):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        return num1, num2

    def almacenar_numero(self):
        num1, num2 = self.pedir_numeros()
        self.objlista.guardar_numero([num1, num2])

    def insertar_valor(self):
        pos = int(input("Posición donde insertar: "))
        val1, val2 = self.pedir_numeros()
        self.objlista.insertar_dato(pos, val1, val2)

    def eliminar_valor(self):
        self.objlista.eliminar_dato()

    def remover_valor(self):
        val1, val2 = self.pedir_numeros()
        self.objlista.remover_dato(val1, val2)

    def index_valor(self):
        val1, val2 = self.pedir_numeros()
        try:
            index = self.objlista.index_dato(val1, val2)
            print(f"El índice del valor {[val1, val2]} es: {index}")
        except ValueError:
            print(f"El valor {[val1, val2]} no se encuentra en la lista.")
    def count_valor(self):
        val1, val2 = self.pedir_numeros()
        count = self.objlista.count_dato(val1, val2)
        print(f"El valor {[val1, val2]} aparece {count} veces en la lista.")
        
    def sort_valor(self):
        self.objlista.sort_dato()
        print("Lista ordenada.")
    
    def reverse_valor(self):
        self.objlista.reverse_dato()
        print("Lista invertida.")
    def agregar_a_tupla_pares(self):
        val = int(input("Ingrese número par para agregar: "))
        self.objlista.agregar_a_tupla_pares(val)

    def eliminar_de_tupla_pares(self):
        val = int(input("Ingrese número par a eliminar: "))
        self.objlista.eliminar_de_tupla_pares(val)

    def modificar_tupla_pares(self):
            print("La tupla de pares actual es:", self.objlista.tupla_pares)
            try:
                viejo = int(input("Ingrese el número par que desea reemplazar: "))
                nuevo = int(input("Ingrese el nuevo número par: "))
            
                index = self.objlista.tupla_pares.index(viejo)
            
                lista_pares = list(self.objlista.tupla_pares)
                lista_pares[index] = nuevo
                self.objlista.tupla_pares = tuple(lista_pares)
                print("Tupla modificada:", self.objlista.tupla_pares)
            except ValueError:
                print("El número no existe en la tupla.")


    def agregar_a_tupla_impares(self):
        val = int(input("Ingrese número impar para agregar: "))
        self.objlista.agregar_a_tupla_impares(val)

    def eliminar_de_tupla_impares(self):
        val = int(input("Ingrese número impar a eliminar: "))
        self.objlista.eliminar_de_tupla_impares(val)

    def modificar_tupla_impares(self):
            print("La tupla de impares actual es:", self.objlista.tupla_impares)
            try:
                viejo = int(input("Ingrese el número impar que desea reemplazar: "))
                nuevo = int(input("Ingrese el nuevo número impar: "))
            
                index = self.objlista.tupla_pares.index(viejo)
            
                lista_pares = list(self.objlista.tupla_pares)
                lista_pares[index] = nuevo
                self.objlista.tupla_pares = tuple(lista_pares)
                print("Tupla modificada:", self.objlista.tupla_pares)
            except ValueError:
                print("El número no existe en la tupla.")
    
    def ver_numero(self):
        self.objlista.ver_numero()


