#Crea un programa que simule las operaciones de un cajero automático. El
#programa debe gestionar un saldo inicial.
#•Debe encapsular la lógica en funciones como consultar_saldo(),
#depositar(), retirar().
#•Utiliza un bucle while para mantener el programa en ejecución hasta que el
#usuario decida salir.
#•Valida las operaciones (ej. no se puede retirar
# más dinero del que hay en el saldo).
#•El código debe ser claro, legible y seguir las recomendaciones de PEP 8.

def consultar_saldo(saldo):

    """
    Esta función nos permite mostrar el salto actual de la cuenta.

    Args:
    saldo (float): Saldo actual de la cuenta.

    """

    print(f"Su saldo actual es: {saldo}")

def depositar(saldo):

    """
    Esta función nos permite depositar el dinero a la cuenta.

    Args:
         saldo (float): Saldo actual de la cuenta antes de depositar.

    Returns:
        float:El nuevo saldo despues del deposito.
    """

    try:
        monto=float(input("Ingrese el monto que desea depositar: "))
        if monto>0:
            saldo=saldo+monto
            print(f"Deposito exitoso. Su nuevo saldo es: {saldo}")
        else:
            print("El monto debe ser mayor a 0.")

    except:
        print("Error: Ingrese un número válido")
    return saldo #Retorna el saldo actualizado o tambien lo retorna sin cambios si hubo errores


def retirar(saldo):

    """
    Esta función permite al usuario retirar el dinero si tiene saldo suficiente.

    Args:
        saldo (float): Saldo actual antes de retirar.

    Returns:
        float:El nuevo saldo despues del retiro.

    """

    try:
        monto=float(input("Ingrese el monto que desea retirar: "))

        if monto<=0:
            print("El monto tiene que ser mayor a 0.")

        elif monto>saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")

        else:
             saldo=saldo-monto
             print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")

    except:
        print("Error: Ingrese un número válido")

    return saldo

def menu():

    """
    Muestra las opciones del menu principal.
    :return:
    """

    print("\n ---CAJERO AUTOMATICO---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

saldo=0.0 #se inicia un saldo en cero

while True:

    menu()#Se llama la función

    opcion=input("Ingrese una opcion del 1 a l 4: ")

    if opcion=="1":
        consultar_saldo(saldo)

    elif opcion=="2":
        saldo=depositar(saldo) #Llama la función para depositar y actualizar el saldo

    elif opcion=="3":
        saldo=retirar(saldo)

    elif opcion=="4":

        print("Gracias por usar nuestro cajero...Saliendo")
        break

    else:
        print("Opción no válida, intente de nuevo")














