import pandas as pd
import os
# Ruta del archivo Excel
archivo_excel = os.path.join(os.getcwd(), 'pedidos_ordenados.xlsx') 
try:
    # Verificar si el archivo existe
    if os.path.exists(archivo_excel):
        print(f"Datos exportados exitosamente a {archivo_excel}")
    else:
        print(f"El archivo {archivo_excel} no existe.")
except Exception as e:
    print(f"Error al verificar el archivo: {e}")