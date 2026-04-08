#  DICOM Auto-Anonymizer Core (HIPAA Safe Harbor)

##  Descripción del Proyecto
Motor algorítmico (*Core*) basado en Inteligencia Artificial y Visión por Computadora para la anonimización automatizada de radiografías maxilofaciales en formato estándar DICOM. 

Este proyecto fue desarrollado para resolver el cuello de botella que representa la limpieza manual de expedientes médicos, garantizando el cumplimiento estricto de la regla de "Puerto Seguro" (*Safe Harbor*) de la ley **HIPAA**. Actúa como una herramienta fundamental de *Privacy by Design* para preparar datasets seguros destinados al entrenamiento de modelos de IA en el sector salud.

##  Características Principales
* **Limpieza de Metadatos:** Extracción y sobrescritura de los 18 identificadores sensibles (ePHI) en las cabeceras del archivo mediante `pydicom`, sin corromper la matriz original.
* **Censura de Texto Incrustado (*Burned-in text*):** Detección y enmascaramiento irreversible de texto sobre los píxeles de la imagen. 
* **Filtros Espaciales:** Uso de umbralización binaria y delimitación de la Región de Interés (ROI) para evitar falsos positivos en las estructuras anatómicas.
* **Alta Eficiencia:** Procesamiento por lotes con una tasa de fuga de información del 0% y tiempos de ejecución ultrarrápidos (**0.66 segundos por imagen**).

##  Tecnologías y Herramientas (Tech Stack)
* **Lenguaje:** Python 3.x
* **Visión por Computadora:** OpenCV (`cv2`)
* **Inteligencia Artificial (OCR):** Tesseract OCR (`pytesseract`)
* **Manejo de Archivos Médicos:** Pydicom

##  Instalación y Requisitos
Asegúrate de tener instalado Python en tu sistema y el motor base de Tesseract OCR. Luego, instala las dependencias necesarias ejecutando:

```bash
pip install pydicom opencv-python pytesseract numpy
