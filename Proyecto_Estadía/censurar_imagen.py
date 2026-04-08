import pydicom
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import matplotlib.pyplot as plt
import time  # <--- IMPORTANTE: Nueva librería para el cronómetro

print("Iniciando escaneo y anonimización...")
tiempo_inicio = time.time()  # <--- INICIA EL CRONÓMETRO

# Conectamos Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrimos la imagen
radiografia = pydicom.dcmread("radiografia_limpia.dcm")
imagen_original = radiografia.pixel_array.copy()
tinta_blanca = int(np.max(imagen_original))
cv2.putText(imagen_original, "PACIENTE: JUAN PEREZ", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, tinta_blanca, 4)

# Preprocesamiento avanzado
imagen_para_ia = cv2.normalize(imagen_original, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
_, imagen_binaria = cv2.threshold(imagen_para_ia, 200, 255, cv2.THRESH_BINARY)
alto_imagen, ancho_imagen = imagen_original.shape

# Inferencia de IA
mapa_datos = pytesseract.image_to_data(imagen_binaria, output_type=Output.DICT, config='--psm 6 --oem 3')

imagen_censurada = imagen_original.copy()
tinta_negra = 0

min_x = ancho_imagen
min_y = alto_imagen
max_x = 0
max_y = 0
found_text = False

zona_segura_superior = alto_imagen * 0.12
limite_horizontal_nombre = ancho_imagen * 0.35

cantidad_palabras = len(mapa_datos['text'])

# PASO 1: Calcular coordenadas del cuadro
for i in range(cantidad_palabras):
    if int(mapa_datos['conf'][i]) > 10:
        x = mapa_datos['left'][i]
        y = mapa_datos['top'][i]
        w = mapa_datos['width'][i]
        h = mapa_datos['height'][i]

        if y < zona_segura_superior and (x + w) < limite_horizontal_nombre and w > 20 and h > 10:
            if x < min_x: min_x = x
            if y < min_y: min_y = y
            if (x + w) > max_x: max_x = x + w
            if (y + h) > max_y: max_y = y + h
            found_text = True

# PASO 2: Dibujar y GUARDAR
if found_text:
    print("¡Nombre detectado! Dibujando máscara de censura...")
    cv2.rectangle(imagen_censurada, (min_x - 15, min_y - 15), (max_x + 15, max_y + 15), tinta_negra, -1)

    # Convertimos la imagen médica a formato estándar (8-bits) antes de guardarla
    imagen_lista_para_guardar = cv2.normalize(imagen_censurada, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    nombre_archivo_salida = "radiografia_segura_HIPAA.png"
    cv2.imwrite(nombre_archivo_salida, imagen_lista_para_guardar)
    print(f" ¡Éxito! Imagen guardada en tu carpeta como: {nombre_archivo_salida}")
else:
    print("No se detectó el bloque de nombre en la zona esperada.")

tiempo_fin = time.time()  # <--- DETIENE EL CRONÓMETRO
tiempo_total = tiempo_fin - tiempo_inicio  # <--- CALCULA LOS SEGUNDOS

print(f"⏱️ Tiempo total de procesamiento: {tiempo_total:.4f} segundos")

# Mostramos el resultado visual final (esto no cuenta en el cronómetro porque es solo para mi)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen_original, cmap=plt.cm.gray)
ax1.set_title("ANTES")
ax2.imshow(imagen_censurada, cmap=plt.cm.gray)
ax2.set_title("DESPUÉS")
plt.show()