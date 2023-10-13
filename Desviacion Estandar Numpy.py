import numpy as np

# Crear un conjunto de datos de ejemplo
datos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calcular la media y la desviación estándar utilizando NumPy
media = np.mean(datos)
desviacion_estandar = np.std(datos)

# Imprimir los resultados
print ("Conjunto de datos:", datos)
print ("Media:", media)
print ("Desviación estándar:", desviacion_estandar)