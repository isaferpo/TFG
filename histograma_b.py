import numpy as np
import matplotlib.pyplot as plt

# Cargar datos desde archivos .npy
reactantsMatrix = np.load('reactantsMatrix.npy')
productsMatrix = np.load('productsMatrix.npy')
reactantsDegree = np.load('reactantsDegree.npy')
productsDegree = np.load('productsDegree.npy')

# Asegurar que son arrays de numpy
reactantsDegree = np.array(reactantsDegree)
productsDegree = np.array(productsDegree)

# ---------- FUNCIONES AUXILIARES ----------

def plot_histogram(degrees, title, color, output_name=None):
    # Calcular histograma
    max_degree = degrees.max()
    bins = range(0, int(max_degree) + 2)
    hist, _ = np.histogram(degrees, bins=bins)
    bin_centers = bins[:-1]

    # Crear figura
    plt.figure(figsize=(10, 6))  # Puedes ajustar el tamaño aquí
    bars = plt.bar(bin_centers, hist, color=color, edgecolor='black', width=0.8)

    # Añadir valores encima de las barras
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            plt.text(bar.get_x() + bar.get_width()/2, height + 1, str(height),
                     ha='center', va='bottom', fontsize=9)

    # Configurar ejes y título
    plt.xlabel("Grado de conectividad")
    plt.ylabel("Número de especies")
    plt.title(title)
    max_y = hist.max()
    plt.yticks(np.arange(0, max_y + 26, 25))  # Escala del eje Y cada 25
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Guardar o mostrar
    if output_name:
        plt.savefig(output_name, dpi=300)
    plt.show()

# ---------- DIBUJAR HISTOGRAMAS ----------

plot_histogram(reactantsDegree, "Histograma de conectividad - Reactivos", color='skyblue')
plot_histogram(productsDegree, "Histograma de conectividad - Productos", color='salmon')
