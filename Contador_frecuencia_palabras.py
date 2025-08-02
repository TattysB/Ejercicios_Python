#Crea una función que reciba un texto (string) y devuelva un diccionario con la
#frecuencia de cada palabra. El diccionario tendrá las palabras como claves y su
#conteo como valor. No debe distinguir entre mayúsculas y minúsculas.

texto=str.lower(input("Digite un texto: ")).split()

frecuencia={}

for palabra in texto:
    frecuencia[palabra]=frecuencia.get(palabra,0)+1 #Se usa el get pára obtener el valor actual(Si no existe, toma 0)y se suma 1

print(frecuencia)
