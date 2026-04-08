import pydicom
# Importamos la herramienta para mostrar gráficos/imágenes
import matplotlib.pyplot as plt

print("Extrayendo la matriz de píxeles...")

# 1. Abrimos nuestro archivo
ruta_archivo = "radiografia_limpia.dcm"
radiografia = pydicom.dcmread(ruta_archivo)

# 2. Extraemos la imagen real (esto saca los píxeles de adentro del archivo)
imagen_pixeles = radiografia.pixel_array

# 3. Configuramos la ventana para mostrar la imagen en escala de grises
plt.imshow(imagen_pixeles, cmap=plt.cm.gray)
plt.title("¡Tu primera radiografía en Python!")

# 4. Le decimos a Python que abra la ventana
print("Abriendo visor de imágenes...")
plt.show()