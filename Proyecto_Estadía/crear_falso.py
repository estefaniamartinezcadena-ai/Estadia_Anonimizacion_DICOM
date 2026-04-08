import pydicom

print("Abriendo archivo base...")
# 1. Leemos el archivo anonimizado
radiografia = pydicom.dcmread("base.dcm")

# 2.
# (En DICOM, los apellidos y nombres se separan con un símbolo ^)
radiografia.PatientName = "Perez Juan Falso"
radiografia.PatientID = "ID-987654321"
radiografia.StudyDate = "20260310" # La fecha se guarda en formato AAAAMMDD

# 3. Guardamos este nuevo archivo modificado con el nombre que queríamos
radiografia.save_as("radiografia_prueba.dcm")

print("¡Listo! Se ha creado el archivo 'radiografia_prueba.dcm' con datos de prueba.")