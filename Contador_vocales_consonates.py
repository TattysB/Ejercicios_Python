#Desarrolla un programa que pida al usuario una frase.
#El programa debe contar cuántas vocales y
#cuántas consonantes contiene la frase (sin contar espacios ni
#símbolos) y mostrar los resultados.


frase=str.lower(input("Ingresa una frase: "))
frase=frase.replace(" ","")
vocal="aeiou"
contador_vocales=0
contador_consonantes=0

def contador (frase):
    """
    Esta función nos sirve para contar cuantas vocales hay en una frase
    y cuantas consonantes hay,esto ignora los espacios y caracteres especiales

    Args:
        frase (str): Texto de la frase
        contador_vocales (int): contador de vocales
        contador_consonantes (int): contador de consonantes
    Returns:
        La cantidad de vocales (int)
        La cantidad de consonantes (int)

    """


for i  in frase:
    if i in vocal:
        contador_vocales+=1
    else :
           contador_consonantes+=1

print(f"Vocales: {contador_vocales} consonantes: {contador_consonantes}")



