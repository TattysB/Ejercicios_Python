#Crea un programa que simule una agenda de contactos. Utiliza un diccionario
#donde las claves sean los nombres de los contactos y los valores sean sus
#números de teléfono. Implementa funciones para:
#1. Añadir un nuevo contacto.
#2. Buscar el teléfono de un contacto por su nombre.
#3. Mostrar todos los contactos.

agenda={} #Diccionario donde se guardaran los contactos


def agregar_contacto(contacto):
    """
    solicita al usuario el nombre y numero de contacto.
    Luego los fuarda en el diccionario que es la agenda.

    Args:

    nombre (str): nombre del contacto

    numero (int): numero del contacto


    Returns:

    str: El nomre del contacto si existe en la agenda.

    int: El numero del contacto si existe en la agenda.


    """

def agregar_contacto(): #función para agregar el contacto
    nombre=str.lower(input(f"Ingrese el nombre del contacto: ").strip()) #.strip()elimina espacios en blanco al principio o al final
    numero=input(f"Ingrese el numero del contacto: ").strip()
    agenda[nombre]=numero #se guarda el contacto en el diccionario:el nombre como clave y el numero como valor
    print(f"El nombre del contacto es {nombre} y su numero es {numero} ,quedo agregado")

def buscar_contacto(): #Función para buscar el contacto
    nombre=input(f"Ingrese el nombre que desea buscar: ").strip()
    if nombre in agenda:
        print(f"El numero es {agenda[nombre]}")
    else:
        print(f"El contacto no existe")

def mostrar_contacto():
    print(f"\n LISTA DE CONTACTOS")

    for nombre,contactos in agenda.items(): #Bucke for para recorrer el diccionario y devuelve una lista
        print(f"{nombre} : {contactos}")

def menu():
    while True:
        print("\n ---MENU DE CONTACTOS---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar contacto")
        print("4. Salir")

        opcion =input("Elija una ocion del 1 al 4 : ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contacto()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")

menu() #se llama a la función


