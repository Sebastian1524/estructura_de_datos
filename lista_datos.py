class Lista_numeros:
    def __init__(self):
        self.lista_numero = []

    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print("Agregado:", dato_numero)

    def incluir_listas(self, otra_lista: list):
        self.lista_numero.extend(otra_lista)

    def insertar_dato(self, posicion: int, valor1: int, valor2: int):
        self.lista_numero.insert(posicion, [valor1, valor2])
        print(f"Insertado {[valor1, valor2]} en la posición {posicion}")

    def eliminar_dato(self):
        try:
            pos = int(input("Ingrese la posición a eliminar: "))
            eliminado = self.lista_numero.pop(pos)
            print(f"Elemento eliminado: {eliminado}")
        except IndexError:
            print("Posición no válida.")

    def remover_dato(self, valor1: int, valor2: int):
        try:
            self.lista_numero.remove([valor1, valor2])
            print(f"Removido: {[valor1, valor2]}")
        except ValueError:
            print(f"El valor {[valor1, valor2]} no se encuentra en la lista.")

    def index_dato(self, valor1: int, valor2: int):
        return self.lista_numero.index([valor1, valor2])

    def ver_numero(self):
        print("Contenido de la lista:", self.lista_numero)
