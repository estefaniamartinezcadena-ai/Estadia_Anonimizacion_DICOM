import pydicom
import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

print("Preparando los pinceles y el motor de IA...")

# 1. Conectamos el cable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. Abrimos nuestra radiografía limpia
radiografia = pydicom.dcmread("radiografia_limpia.dcm")

# Sacamos la matriz de píxeles y le hacemos una copia exacta para poder "rayarla"
imagen_rayada = radiografia.pixel_array.copy()

# 3. Buscamos el color más brillante de la foto para usarlo como tinta blanca
tinta_blanca = int(np.max(imagen_rayada))

# Escribimos el texto en las coordenadas (50, 100) de la imagen
cv2.putText(imagen_rayada, "PACIENTE: JUAN PEREZ", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, tinta_blanca, 4)

# 4. Ajustamos el contraste (normalizamos) para que la IA lo pueda leer clarito
imagen_lista_para_ia = cv2.normalize(imagen_rayada, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# 5. Ponemos a la IA a leer la imagen que acabamos de rayar
print("Escaneando la imagen modificada...")
texto_encontrado = pytesseract.image_to_string(imagen_lista_para_ia)

print("-----------------------------------")
print("🔍 La IA detectó el siguiente texto:")
print(texto_encontrado)
print("-----------------------------------")

# 6. Prendemos el proyector para que ver la evidencia
plt.imshow(imagen_rayada, cmap=plt.cm.gray)
plt.title("Radiografia con Texto Quemado")
plt.show()