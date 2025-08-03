#Desarrolla una función que reciba dos listas y devuelva
# una tupla con tres conjuntos (sets):
#1. Un conjunto con los elementos que están en ambas listas.
#2. Un conjunto con los elementos que solo están en la primera lista.
#3. Un conjunto con los elementos que solo están en la segunda lista.

def elementos_entre_listas(lista_1, lista_2):
    """
    Recibe dos listas y devuelve una tupla con tres conjuntos:

    1.Elementos comunes en ambas listas
    2.Elementos  de la primera lista
    3.Elementos  de la segunda lista

    Args:
        lista_1 (list): Lista 1

        lista_2 (list): Lista 2

    Returns:
        tuple: (comunes,solo_lista1,solo_lista2)

    """

def conjunto_elementos(lista1, lista2):

#convetimos las listas en un cojunto
  set1 = set(lista1)
  set2 = set(lista2)


  comunes=set1 & set2 #Devuelve los elementos que se encuentran en ambas listas

  solo_lista1=set1-set2 #Los elementos que solo estan en la primera lista
  solo_lista2=set2-set1 #Los elementos que estan en la segunda lista

  return comunes;solo_lista1,solo_lista2


lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2=[1,4,5,6,7,8,9,14,15]

resultado=conjunto_elementos(lista1, lista2)
print(f"Lista de los mas comunes: {resultado}")
print(f"Solo lo que esta dentro de la lista 1:  {lista1}")
print(f"Solo lo que esta dentro de la lista 2:  {lista2}")