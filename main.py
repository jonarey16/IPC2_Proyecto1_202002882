from xml.dom.minidom import parse
from xml.etree import ElementTree as ET


class Nodo:
    def __init__(self, value, data):
        self.value = value
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.value)


class Matriz:
    def __init__(self, name: str, m: int, n: int):
        self.name = name
        self.m = m
        self.n = n
        self.row_list = ListaEnlazada()

        count_rows = 0
        while self.n > count_rows:
            row = ListaEnlazada()

            count_cols = 0
            while self.m > count_cols:
                row.add_to_end(None)
                count_cols = count_cols + 1

            self.row_list.add_to_end(row)
            count_rows = count_rows + 1

    def insert(self, x: int, y: int, data):
        row = self.row_list.get_by_index(y)
        row.set_by_index(x, data)

    def get(self, x: int, y: int):
        row = self.row_list.get_by_index(y)
        return row.get_by_index(x)

    def print_matrix(self):
        count = 0
        print(self.name)
        size = self.row_list.get_size()
        while size > count:
            self.row_list.get_by_index(count).print_list()
            count = count + 1
        print()


class ListaEnlazada:
    def __init__(self):
        self.head = None

    # Ver si esta vacío
    def is_void(self):
        return self.head is None

    # Insertar al inicio
    def add_to_head(self, data):
        self.head = Nodo(self.head, data)

    # Insertar al final
    def add_to_end(self, data):
        if self.is_void():
            self.head = Nodo(None, data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Nodo(None, data)

    # Devuelve el tamaño de la lista
    def get_size(self):
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count = count + 1
        return count

    # Devuelve el primer elemento
    def get_first(self):
        if not self.is_void():
            return self.head.data
        else:
            return None

    # Devuelve el ultimo elemento
    def get_last(self):
        if self.is_void():
            return None
        node = self.head
        while node.next is not None:
            node = node.next
        return node.data

    # Devuelve el dato en base al indice
    def get_by_index(self, index: int):
        count = 0
        node = self.head
        while node is not None:
            if index == count:
                return node.data
            count = count + 1
            node = node.next
        return None

    # Añade un elemento en el indice
    def set_by_index(self, index: int, data):
        count = 0
        node = self.head
        while node is not None:
            if index == count:
                node.data = data
                return
            count = count + 1
            node = node.next
        return

    # Elimina el primer elemento de la lista
    def delete_first(self):
        if not self.is_void():
            self.head = self.head.next

    # Elimina el ultimo elemento de la lista
    def delete_last(self):
        if not self.is_void():
            node = self.head
            prev = None
            while node.next is not None:
                prev = node
                node = node.next
            if self.get_size() == 1:
                self.head = None
            else:
                prev.next = None

    # Eliminar indicando el indice
    def delete_by_index(self, index: int):
        if index == 0:
            self.delete_first()
            return
        count = 0
        node = self.head
        prev = None
        while node is not None:
            if index == count:
                prev.next = node.next
            prev = node
            node = node.next
            count = count + 1

    # Vaciar lista enlazada
    def clear(self):
        self.head = None

    # Imprimir Lista
    def print_list(self):
        if not self.is_void():
            node = self.head
            while node is not None:
                print('{}'.format(node.data), end=' | ')
                node = node.next
            print()
        else:
            print('is void')


def lecturaarchivo(data: ListaEnlazada):
    # global domTree, rootNode
    doc = input("Ingrese la ruta del archivo: ")
    domTree = parse(doc)
    root = domTree.documentElement
    terrenos = root.getElementsByTagName("terreno")

    for terreno in terrenos:
        nombre = terreno.getAttribute("nombre")
        dimension = terreno.getElementsByTagName("dimension")[0]
        m = dimension.getElementsByTagName("m")[0].childNodes[0].data
        n = dimension.getElementsByTagName("n")[0].childNodes[0].data

        posicioninicio = terreno.getElementsByTagName("posicioninicio")[0]
        x_i = posicioninicio.getElementsByTagName("x")[0].childNodes[0].data
        y_i = posicioninicio.getElementsByTagName("y")[0].childNodes[0].data

        posicionfinal = terreno.getElementsByTagName("posicionfin")[0]
        x_f = posicionfinal.getElementsByTagName("x")[0].childNodes[0].data
        y_f = posicionfinal.getElementsByTagName("y")[0].childNodes[0].data
        matrizej = Matriz(nombre, int(m), int(n))
        matrizej.print_matrix()
        data.add_to_end(Matriz(nombre, int(m), int(n)))

        posicion = terreno.getElementsByTagName("posicion")
        for element in posicion:
            x = element.getAttribute("x")
            y = element.getAttribute("y")
            pos = element.childNodes[0].data
            # data.get_last().insert(int(x)-1, int(y)-1, pos)


def procesarterreno():
    t = input("Eliga el terreno que quiere procesar")


def mostrar_info():
    print(">> Jonatan David Reyna Monterroso")
    print(">> 202002882")
    print(">> Introducción a la Programación 2 Sección B")
    print(">> Ingeniería en Sistemas")
    print(">> 4to Semestre")


def menu(data: ListaEnlazada):
    ans = True
    while ans:
        print("----------------Bienvenidos--------------")
        print("|    1.Cargar Archivo                   |")
        print("|    2.Procesar Terreno                 | ")
        print("|    3.Escribir Archivo de Salida       |")
        print("|    4.Mostrar Datos del Estudiante     |")
        print("|    5.Generar Gráfica                  |")
        print("|    6.Salir                            |")
        print("-----------------------------------------")
        ans = input("Eliga una opción: ")
        if ans == "1":
            lecturaarchivo(data)
        elif ans == "2":
            procesarterreno()
            print("Archivo procesado con exito")
            print()
        elif ans == "3":
            print("Se escribió la ruta especifica")
        elif ans == "4":
            mostrar_info()
        elif ans == "5":
            print("Grafica generada")
        elif ans == "6":
            print("Cerrando aplicación...")
            ans = False
        else:
            print("Opción inválida\n")


if __name__ == '__main__':
    list_matrix = ListaEnlazada()
    matrix = ListaEnlazada()
    menu(list_matrix)
