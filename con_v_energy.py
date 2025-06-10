import numpy as np
import matplotlib.pyplot as plt
from loki import parseChemFile

def load_energies():
    energy_dict = {}
    with open("databaseStateEnergyHe.txt", 'r') as file:
        for line in file:
            species, energy = line.strip().split()
            energy_dict[species] = float(energy)
    return energy_dict

def plot_connectivity_vs_energy(energy_dict, connectivity, species_names, title):
    x = []
    y = []
    labels = []

    for i, species in enumerate(species_names):
        if species in energy_dict:
            x.append(energy_dict[species])
            y.append(connectivity[i])
            labels.append(species)
        else:
            print(f"⚠️ Warning: '{species}' not found in energy data.")

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='purple', alpha=0.7)

    # Etiquetar puntos significativos
    for xi, yi, label in zip(x, y, labels):
        if yi > np.percentile(y, 95) or xi == min(x) or xi == max(x):
            plt.text(xi, yi, label, fontsize=8, ha='right')

    # Marcar especie con máxima conectividad
    max_idx = np.argmax(y)
    plt.text(x[max_idx], y[max_idx], labels[max_idx],
             fontsize=9, fontweight='bold', color='red')

    plt.title(title)
    plt.xlabel("Energy")
    plt.ylabel("Connectivity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Cargar conectividad (elige según el caso)
    connectivity = np.load("reactantsDegree.npy")  # o "productsDegree.npy"

    # Extraer especies directamente desde el archivo .chem
    species, _ = parseChemFile("helium.chem")

    # Cargar energías desde el archivo especificado
    energies = load_energies()

    # Generar el gráfico
    plot_connectivity_vs_energy(energies, connectivity, species, title="Reactants Connectivity vs Energy")


