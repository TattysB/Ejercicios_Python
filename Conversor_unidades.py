#Escribe un programa que utilice un diccionario para almacenar factores de
#conversión (ej: de metros a pies). Luego, crea una función que reciba una
#cantidad, la unidad de origen y la unidad de destino, y realice la conversión. La
#función debe manejar el caso en que una unidad no exista en el diccionario.

unidades_conversion={

    ('metros', 'pies'):3.28,
    ('kilogramos', 'libras'):2.20,
    ('litros', 'galones'):0.26
} #Este es el diccionario de unidades de conversion

def conversor_unidades():
    """
    Esta funcion convierte una unida de medida a otra utilizando  unidades de medida
    ya definidos.

    Args:

    cantidad (float) : Valor que desea convertir

    unidad_origen (str) : Valor que desea convertir

    unidad_destino (str) : Valor al que se convierte

    Returns:

        resultado (float) : Resultado de la conversion

        None: Si no se encuentra una conversion disponible



    """

def convertir_unidades(cantidad,unidad_origen,unidad_destino): #se define la función y le damos 3 parametros
    lista=(unidad_origen.lower(),unidad_destino.lower()) #Manejo de minisculas

    if lista in unidades_conversion:
        unidad=unidades_conversion[lista]
        return cantidad*unidad #Devuelve el resulado de la conversion es decir la cantidad multiplicada por la munidad
    else:
        return f"Conversion no diponible de la {unidad_origen} a {unidad_destino}" #Si no existe dentro de la lista devuelve un error indicando que no se puede hacer la conversion

try:
    cantidad=float(input("Ingrese la cantidad que desea convertir: "))
    unidad_origen=input("Ingrese la unidad origen: ")
    unidad_destino=input("Ingrese la unidad destino: ")

    resultado=convertir_unidades(cantidad,unidad_origen,unidad_destino) #Se llama la función con los datos que ingresa la persona

    if resultado is not None: #si el resulado es valido (no es None=ausencia),muestra el resultado
        print(f"\n La cantidad que ingreso es {cantidad}, la unidad de origen que ingreso es  {unidad_origen} y esto equivale a {resultado:.2f} {unidad_destino}.")

    else:
        print(f"La conversión que intenta hacer con {unidad_origen} a {unidad_destino} no esta disponible.")

except ValueError:
    print("Error: Ingrese un numero valido")





