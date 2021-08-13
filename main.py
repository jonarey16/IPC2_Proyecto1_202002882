def lecturaarchivo():
    print("Prueba")


def menu():
    ans = True
    while ans:
        print("---------Bienvenidos---------")
        print(" 1.Cargar Archivo")
        print(" 2.Procesar Archivo")
        print(" 3.Escribir Archivo de Salida")
        print(" 4.Mostrar Datos del Estudiante")
        print(" 5.Generar Gráfica")
        print(" 6.Salir")
        ans = input("Eliga una opción: ")
        if ans == "1":
            lecturaarchivo()
            print("Archivo cargado")
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

