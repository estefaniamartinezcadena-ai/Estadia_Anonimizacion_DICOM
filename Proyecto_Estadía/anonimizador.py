import pydicom

print("Iniciando proceso de anonimización (HIPAA Safe Harbor)...")

# 1. Abrimos el archivo que contiene al paciente "Juan Perez Falso"
ruta_original = "radiografia_prueba.dcm"
radiografia = pydicom.dcmread(ruta_original)

print("Paciente original encontrado:", radiografia.PatientName)

# 2. ¡Aplicamos la censura!
# Sobrescribimos las etiquetas con datos genéricos o vacíos
radiografia.PatientName = "ANONIMO PACIENTE"
radiografia.PatientID = "000000"
# Para la fecha, a veces los sistemas fallan si la dejas vacía,
# así que se suele poner una fecha genérica o el 1 de enero del año 1900
radiografia.StudyDate = "19000101"

# 3. Guardamos el resultado en un archivo NUEVO para no dañar el original
ruta_limpia = "radiografia_limpia.dcm"
radiografia.save_as(ruta_limpia)

print("-----------------------------------")
print("¡Éxito! Se ha creado el archivo seguro:", ruta_limpia)
print("Nuevo nombre en el archivo:", radiografia.PatientName)