#Desarrolla un programa que permita al usuario gestionar una lista de compras. El
#programa debe usar un bucle while para mostrar un menú con opciones:
#1. Agregar ítem a la lista.
#2. Eliminar ítem de la lista.
#3. Ver la lista completa.
#4. Salir. El programa debe gestionar la lista de compras y seguir las
#instrucciones del usuario.


def gestinar_compras(menu):
    """
    Esta función nos sirve para agregar,eleiminar y listar un item.

    Args:
        menu (list): Lista con las funciones

         lista_compras (list): Lista vacia donde guarda los item que se agrega

         item (str): Item que se agrega en la lista


    Returns:
        list: Lista con los item que se agrega en la lista


    """


def menu ():
    print(f"\n---LISTA DE COMPRAS---")
    print(f"1. Agregar item a la lista ")
    print(f"2. Eliminar item a la lista ")
    print(f"3. Ver item de la lista ")
    print(f"4. Salir ")

lista_compras = [] #Lista vacia donde se guardaran los item de la compra
while True:
    menu()
    opcion = input("Ingrese una opcion (1-4): ")

    if opcion == "1":
        item =input(f"Ingresa el item que desea agregar: ")
        lista_compras.append(item)
        print(f"El item {item} ha sido agregado a la lista ") #Se confirma que se haya agregado la acción

    elif opcion == "2":
        item=input(f"Ingresa el item que desea eliminar: ")
        if item in lista_compras:
             lista_compras.remove(item) #Se elimina el item
             print(f"El item {item} ha sido eliminado a la lista ")
        else:
            print("El item no existe dentro de la lista")

    elif opcion == "3":
        if lista_compras:
            print(f"\n La lista de compras es: {lista_compras}")
        else:
            print("La lista está vacía")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print(f"Opcion no valida,seleccione del 1 al 4")
