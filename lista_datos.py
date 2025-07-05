
class Lista_numeros:
    def __init__(self):
        self.lista_numero=[]
        
    def guardar_numero(self,dato_numero):
        self.lista_numero.append(dato_numero)
        print(self.lista_numero)
        
    def incluir_listas(self, otra_lista: list):
        self.lista_numero.extend(otra_lista)
        
    def insertar_dato(self, posicion: int, valor1: int, valor2: int):
        self.lista_numero.insert(posicion[valor1, valor2])
        
    def eliminar_dato(self):
        self.lista_numero.pop(int(input("Ingrese la posición a eliminar: ")))
        
        
        
    def ver_numero(self):
        print("Contenido de la lista:", self.lista_numero)