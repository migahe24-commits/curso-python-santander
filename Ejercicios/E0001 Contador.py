#Programa para contar palabras en un archivo de texto
#1. Pedir al usuario la ruta de un archivo de texto
#2. Leer el contenido del archivo
#3. Separar las palabras
#4. Contar numero total de palabras
#5. (Opcional) Mostrar las 10 palabras mas frecuentes y su conteo

archivo = input("Introduce la ruta del archivo de texto: ")

try:
     with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print(f"El archivo especificado no existe")
    exit(1)

# Separar el contenido en palabras
import re
palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)
print(f"Total de palabras: {total_palabras}")

from collections import Counter
contador = Counter(palabras)
mas_comunes = contador.most_common(10)
print("\nLas 10 palabras mas frecuentes son:")
for palabra, conteo in mas_comunes:
    print(f"{palabra}: {conteo}")
print("Fin del programa")
