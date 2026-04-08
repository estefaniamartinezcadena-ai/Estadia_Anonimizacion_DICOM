import pydicom
import cv2  # Esta es la librería OpenCV
import pytesseract  # Este es el cerebro lector
import numpy as np

print("Iniciando el motor de Inteligencia Artificial...")

# 1. Conectamos Python con el programa Tesseract  en Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. Abrimos nuestra radiografía
ruta_archivo = "radiografia_limpia.dcm"
radiografia = pydicom.dcmread(ruta_archivo)
imagen_pixeles = radiografia.pixel_array

# 3. .
# ajustarle el contraste perfecto antes de dársela a leer.
imagen_lista_para_ia = cv2.normalize(imagen_pixeles, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# 4. Le pedimos a la IA que extraiga todo el texto que vea en la imagen
print("Escaneando píxeles en busca de texto...")
texto_encontrado = pytesseract.image_to_string(imagen_lista_para_ia)

print("-----------------------------------")
print("🔍 Texto detectado en la radiografía:")
print(texto_encontrado)
print("-----------------------------------")
