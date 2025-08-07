class Libros:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"Titulo: {self.titulo} -Autor:{self.autor} -Año:{self.anio}")

lista_libros=[]
def agregar_libro():
    titulo=input("Ingrese el titulo del libro: ")
    autor=input("Ingrese el autor del libro: ")
    try:
        anio=int(input("Ingrese el año del libro"))
        if anio<0:
            print("Error, el año no puede ser menor a 0")
        else:
            libro=Libros(titulo, autor, anio)
            lista_libros.append(libro)
            print("El libro se agrego correctamente.")
    except ValueError:
        print("Error al ingresar el año del libro, inténtelo de nuevo")
    except Exception as e:
        print("Ocurrio un error inesperado, intente de nuevo")


def mostrar_libros():
    if not lista_libros:
        print("No existen libros registrados.")
    else:
        print("\n--Lista de Libros--")
        contador=1
        for libro in lista_libros:
            print(f"Libro No.{contador}")
            libro.mostrar_info()
            contador+=1

def eliminar_libro():
    libro_buscado=input("Ingrese el nombre del libro que desea eliminar: ")
    encontrado=False
    for libro in lista_libros:
        if libro.nombre.lower()== libro_buscado.lower():
            lista_libros.remove(libro)
            print("Libro eliminado correctamente.")
            encontrado=True
            break
    if not encontrado:
        print("El libro que deseas eliminar no fue encontrado.")


def menu():
    print("1.Agregar libros")
    print("2.Mostrar lista de libros")
    print("3.Eliminar libros por titulo")
    print("4.Salir")


while True:
    menu()
    option=int(input("\nSeleccione una opción del menú (1-4"))
    match option:
        case "1":
            agregar_libro()
        case "2":
            mostrar_libros()
        case "3":
            eliminar_libro()
        case "4":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Error al seleccionar una opción, inténtelo de nuevo")