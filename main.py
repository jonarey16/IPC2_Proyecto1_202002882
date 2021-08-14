import xml.etree.ElementTree as ET


def lecturaarchivo(ruta):
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    for x in myroot[0]:
        print(x.tag,x.attrib)

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
            print("Archivo cargado\n")
        elif ans == "2":
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

