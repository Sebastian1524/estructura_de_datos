class Calculadora:
    def pedir_numero(self):
        numero1 = input("Ingrese 1:")
        numero2 = input("Ingrese 2:")
        return numero1, numero2
    def almacenar_numero(self):
        dato_numero = [self.numero1, self.numero2]
        self.objlista.guardar_numero(dato_numero)