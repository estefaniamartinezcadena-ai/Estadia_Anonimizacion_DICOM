import pydicom

# 1. Le decimos a Python el nombre del archivo que fabricamos en el paso anterior
ruta_archivo = "radiografia_prueba.dcm"

# 2. Leemos el archivo y extraemos toda su información
radiografia = pydicom.dcmread(ruta_archivo)

# 3. Imprimimos los datos en la pantalla para comprobar que ahí están
print("¡Archivo leído con éxito! ")
print("-----------------------------------")
print("Nombre del paciente:", radiografia.PatientName)
print("ID del paciente:", radiografia.PatientID)
print("Fecha del estudio:", radiografia.StudyDate)