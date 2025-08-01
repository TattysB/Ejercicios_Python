#Crea una función que reciba una lista de calificaciones (números). La función
#debe calcular y retornar el promedio, la calificación más alta y la más baja en una
#tupla. Luego, escribe el código para probar esta función con una lista de ejemplo.


cantidad = int(input("Ingrese la cantidad de notas: "))

def cantidad(cantidad):
    """
    Esta función valida que la cantidad de notas que ingresa el usuario
    y saca la nota mas bajita,mas alta y el promedio.

    Args:
    cantidad (int): cantidad de notas

    notas (float): notas que ingresa el usuario

    nota (list): lista de notas que ingresa el usuario

    Returns:
        La nota mas bajida (float)

        La nota mas alta (float)

        El promedio de las notas (float)

        La lista de notas que ingresa el usuario (list)

    """

def calificacion():

   notas=[]

   for i in range(cantidad):
       nota=float(input("Ingrese la nota del: "))
       while nota<0 or nota>5:
           print("La nota debe estar entre 0 y 5")
           nota=float(input("Ingrese la nota del: "))
           nota[i]=nota
           return
       notas.append(nota) #Cada vez que el usuario ingresa una nota se guarda en una lista

       max_nota=max(notas)
       min_nota=min(notas)
       media_nota=sum(notas)/len(notas)


   print(f"La nota mas baja es de: {min_nota}")
   print(f"La nota mas alta es de: {max_nota}")
   print(f"El promedio de notas es de: {media_nota}")
   print(f"Las notas ingresadas fueron: {notas}")

calificacion()



