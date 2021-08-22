import xml.etree.ElementTree as ET


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0

    def Append(self, Value):
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        else:
            Current = self.First
            while Current.next != None:
                Current = Current.next
            Current.next = MyNode

        self.Size += 1
        return MyNode

    def __len__(self):
        return self.Size

    def __str__(self):
        String = "["
        Current = self.First
        for i in range(len(self)):
            String += str(Current)
            if i != len(self) - 1:
                String += str(", ")
            Current = Current.next
        String += "]"
        return String


def lecturaarchivo(ruta):
    global tree, root
    try :
        tree = ET.parse(ruta)
        root = tree.getroot()
        print("Archivo cargado\n")
    except:
        print("Archivo Invalido --> Debe de ser un archivo .xml")



def procesarterreno():
    t = input("Eliga el terreno que quiere procesar")


def menu():
    ans = True
    while ans:
        print("----------------Bienvenidos--------------")
        print("|    1.Cargar Archivo                   |")
        print("|    2.Procesar Archivo                 | ")
        print("|    3.Escribir Archivo de Salida       |")
        print("|    4.Mostrar Datos del Estudiante     |")
        print("|    5.Generar Gráfica                  |")
        print("|    6.Salir                            |")
        print("-----------------------------------------")
        ans = input("Eliga una opción: ")
        if ans == "1":
            ruta = input("Ingrese la ruta del archivo: ")
            lecturaarchivo(ruta)
        elif ans == "2":
            procesarterreno()
            print("Archivo procesado con exito")
            print()
        elif ans == "3":
            print("Se escribió la ruta especifica")
        elif ans == "4":
            print("Datos del estudiante")
        elif ans == "5":
            print("Grafica generada")
        elif ans == "6":
            print("Cerrando aplicación...")
            ans = False
        else:
            print("Opción inválida\n")


if __name__ == '__main__':
    menu()
