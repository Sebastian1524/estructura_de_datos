from lista_datos import Lista_numeros

class Calculadora:
    
    def __init__(self):
        self.objlista = Lista_numeros()
        self.numero1 = ""
        self.numero2 = ""
        
    def pedir_numero(self):
        numero1 = int(input("Ingrese 1:"))
        numero2 = int(input("Ingrese 2:"))
        return numero1, numero2
    
    
    def almacenar_numero(self):
        self.numero1, self.numero2 = self.pedir_numero()
        data_numero = [self.numero1, self.numero2]
        self.objlista.guardar_numero(data_numero)

        
    def insertar_valor(self):
        pos = int(input("Posición donde insertar: "))
        val1 = int(input("Valor 1 a insertar: "))
        val2 = int(input("Valor 2 a insertar: "))
        self.objlista.insertar_dato(pos, val1, val2)
        self.ver_numero()
    
    def eliminar_valor(self):
        self.objlista.eliminar_dato()
        self.ver_numero()
        
    def ver_numero(self):
        self.objlista.ver_numero()


if __name__ == "__main__":
    calc = Calculadora()
    calc.almacenar_numero()
    calc.insertar_valor()
