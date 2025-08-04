#1. Define una estructura de datos principal: un diccionario de estudiantes.
#Las claves serán los nombres de los estudiantes y los valores serán listas
#con sus calificaciones.
#2.Crea una función calcular_promedio(calificaciones) que reciba una lista de
#números y devuelva su promedio.
#3.Crea una función obtener_estado(promedio) que devuelva "Aprobado" si el
#promedio es mayor o igual a 3.0, y "Reprobado" en caso contrario.
#4.Crea una función principal generar_reporte(estudiantes) que itere sobre el
#diccionario de estudiantes. Para cada uno, debe llamar a las funciones
#anteriores e imprimir un reporte formateado, como:
#5.Reporte de Calificaciones:
#6.-------------------------
#7.- Estudiante: Ana, Promedio: 4.5, Estado: Aprobado
#38.- Estudiante: Juan, Promedio: 2.8, Estado: Reprobado
#9.-------------------------
#10todo el script debe estar comentado, con docstrings en cada función
#explicando qué hace, qué recibe y qué devuelve. La nomenclatura de
#variables y funciones debe seguir PEP 8.

def calcular_promedio(calificaciones):

    """
    Esta función calcula el promedio de una lista de calificaciones

    Args:
        calificaciones (list of float): Lista de notas del estudiante

    Returns:
        float: Promedio del estudiante

    """

    suma=sum(calificaciones) #Suma todas las calificaciones que estan en la lista
    cantidad=len(calificaciones) #Cuenta cuantas calificaciones han ingresado
    promedio=suma/cantidad #Divide la suma por la cantidad de las notas que ha ingresado

    return promedio #retorna el resultado

def obtener_estado(promedio):

    """
    Esta función nos permite saber si el estudiante aprobro o reprobo.

    Args:
        promedio (float): Promedio notas del estudiante

    Returns:
        str: Estado del estudiante
    """


    if promedio>=3.0:
        return "Aprobado"

    else:
        return "Reprobado"

def generar_reporte(estudiantes):

    """
    Esta función nos permite generar e imprimir el reporte de calificaciones de un estudiante.

    Args:
         estudiantes (dict) : Diccionario con nombre como claves y listas de calificaciones como valores

    Returns:
        None
    """

    print("\n---REPORTE DE CALIFICACIONES---")
    print("-------------------------------------")

    for nombre,notas in estudiantes.items(): #recorre a cada estudiante y sus calificaciones en el diccionario
        promedio=calcular_promedio(notas) # se calcula el promedio
        estado=obtener_estado(promedio) #se determina en el estado

        print(f"Estudiante: {nombre}, Promedio: {promedio}, Estado: {estado}")

    print("-------------------------------------")

#donde le pedimos aal usuario sus datos
estudiantes={} #Diccionario vacio para almacenar a los estudiantes y las notas

while True:
    try:
      cantidad=int(input("¿Cuantos estudiantes desea ingresar?: "))
      if cantidad<=0:
           print("Debe ingresar un numero mayor a 0")
      else:
       break

    except ValueError:
     print("Error: Ingres un numero valido")


for i in range(cantidad):
    nombre=input(f"Ingrese el nombre del estudiante {i+1}: ")

    while True:
        try:
         num_notas=int(input(f"¿Cuantas notas tiene? {nombre}: "))

         if num_notas<=0:
             print("Debe ingresar al menos una nota")
         else:
             break
        except :
            print("Error: Ingres un numero valido")

    notas=[] #Se crea una lista para almacenar las notas

    for j in range(num_notas): #Se inicia otro ciclo paara ingresar las notas
        while True:
            try:
             nota=float(input(f"Ingrese la nota {j+1} entre 0.0 y 5.0:  "))
             if 0.0<=nota<=5.0:
                 notas.append(nota)
                 break
             else:
               print("La nota debe estar entre 0.0 y 5.0")
            except ValueError:
                print("Error: Ingres un numero valido")

        notas.append(nota) #Se agrega la nota a la lista

    estudiantes[nombre]=notas #Se asocia la lista de notas con el nombre del estudiante


generar_reporte(estudiantes)