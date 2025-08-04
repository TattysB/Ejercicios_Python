#Diseña un sistema para gestionar el inventario de una tienda. El inventario se
#almacenará en una lista de diccionarios. Cada diccionario representará un
#producto con "nombre", "precio" y "cantidad". El programa debe:
#•Usar funciones para cada operación: agregar_producto(),
# realizar_venta(),mostrar_inventario().
#•La función realizar_venta debe actualizar la cantidad del producto vendido.
#•El código debe estar bien documentado con
# docstrings y seguir la nomenclatura de PEP 8.
#•Mostrar un menú interactivo para el usuario.

inventario=[] #Lista vacia que almacenara cada producto

def agregar_producto(precio,cantidad):

    """
    Agrega un nuevo producto al inventario.

    Solicita a la persona el nombre,precio y cantidad del producto,
    luego lo agrega como un diccionario a la lista de inventario

    Args:
        precio (float): precio del producto
        cantidad (int): cantidad del producto


    """
    nombre=input("Ingrese el nombre del producto: ").strip()

    try:
        precio=float(input("Ingrese el precio : "))
        cantidad=int(input("Ingrese la cantidad : "))

        producto={"nombre":nombre,"precio":precio,"cantidad":cantidad} #Se crea el diccionario con los datos del producto

        inventario.append(producto)#Agregamos el producto a la lista del inventario

        print("Producto agregado con exito.")

    except ValueError:
        print("Valores numericos no válidos para precio y cantidad.")


def realizar_venta(cantidad_vendida):

    """
    Realiza una venta y actualiza la cantidad del producto en el inventario.

    Solicita el nombre del producto y la cantidad a vender.
    Si el producto existe y hay sufuciente cantidad,el inventario se actualiza.

    Args:
        cantidad_vendida (int): cantidad del producto

    """
    nombre=input("Ingrese el nombre del producto que se va a vender: ").strip()

    try:
        cantidad_vendida=int(input("Ingrese la cantidad que se va a vender: "))

        for producto in inventario:
            if producto["nombre"].lower() == nombre.lower():
                if producto["cantidad"] >= cantidad_vendida:
                    producto["cantidad"] -= cantidad_vendida #Se resta lo que se vendio
                    total = cantidad_vendida * producto["precio"] #Se calculaa el total a pagar
                    print(f"Se  realizo la venta por un total de : ${total:,d}") #Se muestra el total
                    return #Salimos de la función despues de realizar una venta
            else:
                print("No hay suficientes productos para la venta.")
                return
        print("El producto no se encontro.") #Si no se encuentra el producto en el inventario

    except ValueError:
         print("Error: Ingresa un valor valido para la cantidad.")


def mostrar_inventario():

    """
    Muestra todos los productos disponibles en el inventario.

    Recorre la lista de procustos e imprime nombre,precio y cantidad del producto.


    """

    if not inventario:#Si la lista llega estar vacia se manda un mensaje
        print("El inventario esta vacío")
        return #salimos de la funcion

    print("\n  El inventario actual es: ")

    for producto in inventario:
        print(f"Nombre: {producto['nombre']}  {producto['precio']}  {producto['cantidad']} unidades",sep='|')
    print() #Linea en blanco se realiza por estetica para que no quede pegado


def menu():
    """
    Muestra el menu principal y interactua con el usuario hasta que el decida salir.


    """

    while True:
        print("--Menu de inventario--")
        print("1.Agregar producto")
        print("2.Realizar venta")
        print("3.Mostrar inventario")
        print("4.Salir")

        opcion=input("Elija una opcion del 1 al 4: ")
        print()

        if opcion=="1":
            agregar_producto()
        elif opcion=="2":
            realizar_venta()
        elif opcion=="3":
            mostrar_inventario()
        elif opcion=="4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida.Intente nuevamente")

menu()




