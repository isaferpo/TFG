import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
reactantsMatrix = np.load('reactantsMatrix.npy')
productsMatrix = np.load('productsMatrix.npy')
reactantsDegree = np.load('reactantsDegree.npy')
productsDegree = np.load('productsDegree.npy')

# Asegurar arrays numpy
reactantsDegree = np.array(reactantsDegree)
productsDegree = np.array(productsDegree)

# Definir bins comunes
max_degree = max(reactantsDegree.max(), productsDegree.max())
bins = range(0, int(max_degree) + 2)  # Bins enteros: 0, 1, 2, ..., max_degree

# Calcular histogramas
reactants_hist, _ = np.histogram(reactantsDegree, bins=bins)
products_hist, _ = np.histogram(productsDegree, bins=bins)
bin_centers = bins[:-1]  # Para etiquetar las barras

# Crear subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Histograma de Reactivos
ax1.bar(bin_centers, reactants_hist, color='skyblue', edgecolor='black', width=7)
ax1.set_title("Reactivos")
ax1.set_xlabel("Grado de conectividad")
ax1.set_ylabel("Número de especies")
ax1.grid(True, linestyle='--', alpha=0.6)
max_y = max(reactants_hist.max(), products_hist.max())
ax1.set_yticks(np.arange(0, max_y + 26, 25))

# Histograma de Productos
ax2.bar(bin_centers, products_hist, color='salmon', edgecolor='black', width=7)
ax2.set_title("Productos")
ax2.set_xlabel("Grado de conectividad")
ax2.grid(True, linestyle='--', alpha=0.6)

# Mostrar ambos
plt.suptitle("Comparativa de grados de conectividad por especie")
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajustar para el título
plt.show()
