class Lista_numeros:
    def __init__(self):
        self.lista_numero = []
        self.tupla_pares = ()
        self.tupla_impares = ()
    
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
    
    def count_dato(self, valor1: int, valor2: int):
        return self.lista_numero.count([valor1, valor2])
    
    def sort_dato(self):
        self.lista_numero.sort()
        print("Lista ordenada:", self.lista_numero)
        
    def reverse_dato(self):
        self.lista_numero.reverse()
        print("Lista invertida:", self.lista_numero)

    def ver_numero(self):
        print("Contenido de la lista:", self.lista_numero)

    def actualizar_tuplas(self):
        numeros_planos = [n for sublista in self.lista_numero for n in sublista]
        self.tupla_pares = tuple(n for n in numeros_planos if n % 2 == 0)
        self.tupla_impares = tuple(n for n in numeros_planos if n % 2 != 0)
        
    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print("Agregado:", dato_numero)
        self.actualizar_tuplas()
    
    def agregar_a_tupla_pares(self, valor):
        if valor % 2 == 0:
            lista = list(self.tupla_pares)
            lista.append(valor)
            self.tupla_pares = tuple(lista)
            print("Agregado a tupla de pares:", self.tupla_pares)
        else:
            print("Solo se permiten números pares.")

    def eliminar_de_tupla_pares(self, valor):
        lista = list(self.tupla_pares)
        try:
            lista.remove(valor)
            self.tupla_pares = tuple(lista)
            print("Eliminado de tupla de pares:", self.tupla_pares)
        except ValueError:
            print("El valor no está en la tupla de pares.")

    def modificar_tupla_pares(self, posicion, nuevo_valor):
        if nuevo_valor % 2 == 0:
            lista = list(self.tupla_pares)
            try:
                lista[posicion] = nuevo_valor
                self.tupla_pares = tuple(lista)
                print("Modificada tupla de pares:", self.tupla_pares)
            except IndexError:
                print("Posición inválida.")
        else:
            print("Solo se permiten números pares.")


    def agregar_a_tupla_impares(self, valor):
        if valor % 2 != 0:
            lista = list(self.tupla_impares)
            lista.append(valor)
            self.tupla_impares = tuple(lista)
            print("Agregado a tupla de impares:", self.tupla_impares)
        else:
            print("Solo se permiten números impares.")

    def eliminar_de_tupla_impares(self, valor):
        lista = list(self.tupla_impares)
        try:
            lista.remove(valor)
            self.tupla_impares = tuple(lista)
            print("Eliminado de tupla de impares:", self.tupla_impares)
        except ValueError:
            print("El valor no está en la tupla de impares.")

    def modificar_tupla_impares(self, posicion, nuevo_valor):
        if nuevo_valor % 2 != 0:
            lista = list(self.tupla_impares)
            try:
                lista[posicion] = nuevo_valor
                self.tupla_impares = tuple(lista)
                print("Modificada tupla de impares:", self.tupla_impares)
            except IndexError:
                print("Posición inválida.")
        else:
            print("Solo se permiten números impares.")
