#Crea un juego donde el programa "piensa" un número secreto entre 1 y 100
#(puedes definirlo estáticamente, por ejemplo, numero_secreto = 42). El usuario
#debe adivinarlo. En cada intento, el programa le dirá si el número ingresado es
#mayor o menor que el número secreto. El juego termina cuando el usuario adivina
#el número.

numero_secreto= 15

def adivinar_numero():
    """
    Esta función permite al usuario adivinar un número secreto entre 1 y 100.
    El usuario recibe pistas si su intento es mayor o menor que el número secreto.

     Args:
        numero_usuario (int): Numero a adivinar

    Returns:
        El numero adivinado (int)
    """
while True:
    usuario = int(input("Ingrese el numero secreto del 1 al 100: "))
    if usuario > 1 and usuario < 100:
        if usuario < numero_secreto:
            print("El numero  es mayor")
        elif usuario > numero_secreto:
            print("El numero es menor")
        else :
            print(f"El número secreto era {numero_secreto} felicitaciones!!!!!!")
            break
    else:
        print("Ingrese un numero dentro del rango de 1 y 100")
