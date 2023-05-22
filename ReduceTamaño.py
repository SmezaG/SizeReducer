from PIL import Image
import os
import argparse
import tkinter as tk
from tkinter import filedialog


def reducir_peso_imagen(archivo_entrada, archivo_salida, calidad=85):
    # Abrir la imagen original
    imagen = Image.open(archivo_entrada)
    
    # Guardar la imagen con la calidad especificada
    imagen.save(archivo_salida, optimize=True, quality=calidad)
    
    # Obtener el tamaño de archivo original y el tamaño después de la compresión
    tamano_original = os.path.getsize(archivo_entrada)
    tamano_comprimido = os.path.getsize(archivo_salida)
    
    # Calcular el porcentaje de reducción
    porcentaje_reduccion = (tamano_original - tamano_comprimido) / float(tamano_original) * 100
    
    print("Tamaño original: {} bytes".format(tamano_original))
    print("Tamaño comprimido: {} bytes".format(tamano_comprimido))
    print("Reducción de tamaño: {:.2f}%".format(porcentaje_reduccion))


def comprimir_imagenes_carpeta(ruta_carpeta, calidad=85):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)
    
    # Filtrar solo los archivos de imagen
    imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Comprimir cada imagen en la carpeta
    for imagen in imagenes:
        ruta_imagen = os.path.join(ruta_carpeta, imagen)
        ruta_imagen_comprimida = os.path.join(ruta_carpeta, "comprimida_" + imagen)
        
        reducir_peso_imagen(ruta_imagen, ruta_imagen_comprimida, calidad=calidad)
        
        # Reemplazar el archivo original con el archivo comprimido
        os.replace(ruta_imagen_comprimida, ruta_imagen)


def seleccionar_carpeta():
    root = tk.Tk()
    root.withdraw()
    ruta_carpeta = filedialog.askdirectory()
    return ruta_carpeta


# Crear el parser de argumentos
parser = argparse.ArgumentParser(description='Compresión de imágenes en una carpeta')
parser.add_argument('--calidad', type=int, default=85, help='Calidad de compresión (valor por defecto: 85)')

# Obtener los argumentos del programa
args = parser.parse_args()

# Obtener la ruta de la carpeta mediante el selector de carpetas
ruta_carpeta = seleccionar_carpeta()

# Ejecutar la función con los argumentos proporcionados
comprimir_imagenes_carpeta(ruta_carpeta, calidad=args.calidad)
