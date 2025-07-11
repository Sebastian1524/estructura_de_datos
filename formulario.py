from lista_datos import Lista_numeros

class Calculadora:
    def __init__(self):
        self.objlista = Lista_numeros()

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

    def ver_numero(self):
        self.objlista.ver_numero()

