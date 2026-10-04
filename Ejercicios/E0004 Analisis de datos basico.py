#Analisis de datos basico
#Si te sientes con ánimos, intenta usar Cursor en un mini análisis de datos:
#Consigue un pequeño conjunto de datos, por ejemplo un CSV con dos columnas de números (puedes crearlo manualmente).
#Escribe un script analisis.py que lea el CSV (utiliza pandas si quieres, Cursor te ayudará a importarlo y usarlo).
#Calcula estadísticas simples: media, mediana, desviación estándar de cada columna.
#Genera una gráfica de dispersión de una columna vs. la otra (aquí tendrás que usar matplotlib; prueba a pedirle a Cursor "Traza un scatter plot de col1 vs. col2").
#Observa cómo la IA incluso puede escribir el código de Matplotlib para ti.
#Ejecuta el script; si estás en Cursor, la gráfica debería abrirse en una ventana externa (o en el panel de plot de VS Code si está habilitado).
#Este ejercicio mezcla programación con un toque de data science, exhibiendo la versatilidad de Cursor.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el CSV
df = pd.read_csv('datos.csv')

# Calcular estadísticas simples
media = df.mean()
mediana = df.median()
desviacion = df.std()

# Generar gráfica de dispersión de una columna vs. la otra
plt.scatter(df['col1'], df['col2'])
plt.show()

print(media)
print(mediana)
print(desviacion)

print("Fin del programa")