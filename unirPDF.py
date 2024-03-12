import os
from PyPDF2 import PdfReader, PdfWriter

# Función para fusionar archivos PDF uno por uno en orden
def fusionar_archivos(ruta_carpeta1, ruta_carpeta2, carpeta_salida):
    # Obtener la lista de archivos en ambas carpetas
    archivos_carpeta1 = sorted([archivo for archivo in os.listdir(ruta_carpeta1) if archivo.endswith('.pdf')])
    archivos_carpeta2 = sorted([archivo for archivo in os.listdir(ruta_carpeta2) if archivo.endswith('.pdf')])
    
    # Asegurarse de que ambas carpetas tengan el mismo número de archivos
    if len(archivos_carpeta1) != len(archivos_carpeta2):
        print("Las carpetas no contienen el mismo número de archivos PDF.")
        return
    
    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    
    # Fusionar los archivos uno por uno en orden
    for i in range(len(archivos_carpeta1)):
        archivo_carpeta1 = os.path.join(ruta_carpeta1, archivos_carpeta1[i])
        archivo_carpeta2 = os.path.join(ruta_carpeta2, archivos_carpeta2[i])
        
        with open(archivo_carpeta1, 'rb') as file1, open(archivo_carpeta2, 'rb') as file2:
            reader1 = PdfReader(file1)
            reader2 = PdfReader(file2)
            writer = PdfWriter()
            
            # Agregar todas las páginas del primer archivo
            for page in reader1.pages:
                writer.add_page(page)
            
            # Agregar todas las páginas del segundo archivo
            for page in reader2.pages:
                writer.add_page(page)
            
            # Guardar el archivo fusionado en la carpeta de salida
            ruta_salida = os.path.join(carpeta_salida, f"{i+1}.pdf")
            with open(ruta_salida, 'wb') as file_salida:
                writer.write(file_salida)

# Rutas de las carpetas que quieres fusionar
ruta_carpeta_documentos = 'C:\Python\Facturas venta'
ruta_carpeta_facturas = 'C:\Python\Documentos'


# Carpeta de salida para los archivos fusionados
carpeta_salida = 'C:\Python\pdf unificados'

# Llamar a la función para fusionar los archivos
fusionar_archivos(ruta_carpeta_documentos, ruta_carpeta_facturas, carpeta_salida)
