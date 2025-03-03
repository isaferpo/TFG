# Importar el módulo necesario para trabajar con archivos
import os
import re

# Definir la ruta del archivo
file_path = 'C:/Users/Usuario/OneDrive/Desktop/Escritorio/FÍSICA/último año-DESKTOP-AO49550/TFG/helium.chem'
output_path = 'C:/Users/Usuario/OneDrive/Desktop/Escritorio/FÍSICA/último año-DESKTOP-AO49550/TFG/helium_cleaned.chem'

# Leer el archivo y aplicar strip() a cada línea
with open(file_path, 'r') as file:
    lines = file.readlines()

# Aplicar strip() a cada línea
blank_lines = [line.strip() for line in lines]
# Eliminar lineas comentadas y vacías con un if
# Buscar todos los elementos que contienen He y e
for line in blank_lines:
    pattern = re.compile(r'He\([^\)]+\)|e')
trimmed_lines = [pattern.findall(line) for line in blank_lines]

# Eliminar los elementos repetidos
unique_lines = set()
for line in trimmed_lines:
    unique_lines.update(line)

# Crear un nuevo documento con los elementos ordenados
with open(output_path, 'w') as file:
    for item in unique_lines:
        file.write(f"{item}\n")

print("Archivo limpio creado en:", output_path)