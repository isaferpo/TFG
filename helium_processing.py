import re

# Definir la ruta del archivo
file_path = 'little_helium.txt'
output_path = 'helium_prueba.txt'

# Leer el archivo y eliminar líneas comentadas y vacías
with open(file_path, 'r') as file:
    lines = file.readlines()

# Filtrar las líneas: eliminar comentarios (%) y tomar solo la parte antes de '|'
filtered_lines = []
for line in lines:
    line = line.strip()  # Eliminar espacios en blanco al inicio y al final
    if line and not line.startswith('%'):  # Verificar que no esté vacía ni sea un comentario
        filtered_lines.append(line.split('|')[0])  # Tomar solo la parte antes de '|'

# Aplicar la expresión regular para extraer elementos específicos
pattern = re.compile(r'(->|<->|e|He2?\([^\)]+\))')

extracted_lines = []
for line in filtered_lines:
    matches = pattern.findall(line)  # Buscar coincidencias en la línea
    extracted_lines.append(" ".join(matches))  # Unir las coincidencias en una sola línea

# Guardar el resultado en un nuevo archivo de texto
with open(output_path, 'w') as file:
    file.writelines("\n".join(extracted_lines))

print("Archivo limpio creado en:", output_path)