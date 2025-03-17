import os
import re

# Definir la ruta del archivo
file_path = os.path.join(os.getcwd(), 'TFG', 'helium.chem')
output_path = os.path.join(os.getcwd(), 'TFG', 'helium_clean.txt')

# Leer el archivo y eliminar líneas comentadas y vacías
with open(file_path, 'r') as file:
    lines = file.readlines()

# Filtrar las líneas que contienen flechas, 'e' y 'He(...)', y eliminar las líneas que comienzan con %, espacios en blanco y barras
pattern = re.compile(r'(->|<->|e|He\([^\)]+\))')
clean_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('%') and not line.strip().startswith('|') and pattern.search(line)]

# Extraer solo los elementos e, +, flechas o He(...)
extracted_lines = []
for line in clean_lines:
    matches = pattern.findall(line)
    extracted_lines.append(" ".join(matches))

# Guardar el resultado en un nuevo archivo de texto
with open(output_path, 'w') as file:
    file.writelines("\n".join(extracted_lines))

print("Archivo limpio creado en:", output_path)

print("Archivo limpio creado en:", output_path)