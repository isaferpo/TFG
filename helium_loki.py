import loki as lk
import pandas as pd
import matplotlib.pyplot as plt

def main(file):
    # Parsear el archivo químico
    uniqueSpecies, reactions = lk.parseChemFile(file)

    # Crear una lista de especies únicas
    speciesList = sorted(uniqueSpecies)  # Ordenar para consistencia

    # Inicializar matrices de incidencia para reactivos y productos
    reactantsMatrix = []
    productsMatrix = []

    # Construir las matrices de incidencia
    for reaction in reactions:
        # Inicializar filas para la reacción actual
        reactantsRow = [0] * len(speciesList)
        productsRow = [0] * len(speciesList)

        # Llenar la fila de reactivos
        for idx, species in enumerate(speciesList):
            if species in reaction['lhsSpecies']:
                reactantsRow[idx] = reaction['lhsStoichiometricCoeffs'][reaction['lhsSpecies'].index(species)]

        # Llenar la fila de productos
        for idx, species in enumerate(speciesList):
            if species in reaction['rhsSpecies']:
                productsRow[idx] = reaction['rhsStoichiometricCoeffs'][reaction['rhsSpecies'].index(species)]

        # Agregar las filas a las matrices
        reactantsMatrix.append(reactantsRow)
        productsMatrix.append(productsRow)

    # Representar las matrices de incidencia con imshow
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Matriz de reactivos
    axes[0].imshow(reactantsMatrix, cmap='Blues', aspect='auto')
    axes[0].set_title("Matriz de Incidencia - Reactivos")
    axes[0].set_xlabel("Especies")
    axes[0].set_ylabel("Reacciones")
    axes[0].set_xticks(range(len(speciesList)))
    axes[0].set_xticklabels(speciesList, rotation=90)
    axes[0].set_yticks(range(len(reactions)))
    axes[0].set_yticklabels([f"R{i+1}" for i in range(len(reactions))])

    # Matriz de productos
    axes[1].imshow(productsMatrix, cmap='Oranges', aspect='auto')
    axes[1].set_title("Matriz de Incidencia - Productos")
    axes[1].set_xlabel("Especies")
    axes[1].set_ylabel("Reacciones")
    axes[1].set_xticks(range(len(speciesList)))
    axes[1].set_xticklabels(speciesList, rotation=90)
    axes[1].set_yticks(range(len(reactions)))
    axes[1].set_yticklabels([f"R{i+1}" for i in range(len(reactions))])

    # Ajustar diseño y mostrar las matrices
    plt.tight_layout()
    plt.show()

    # Calcular el grado de los nodos (degree node) para las especies
    reactantsDegree = [sum(col) for col in zip(*reactantsMatrix)]  # Suma de cada columna (grado en reactivos)
    productsDegree = [sum(col) for col in zip(*productsMatrix)]    # Suma de cada columna (grado en productos)

    # Crear histogramas del grado de los nodos
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Histograma para los reactivos
    axes[0].bar(speciesList, reactantsDegree, color='blue', alpha=0.7)
    axes[0].set_title("Grado de Nodos - Reactivos")
    axes[0].set_xlabel("Especies")
    axes[0].set_ylabel("Grado")
    axes[0].tick_params(axis='x', rotation=90)

    # Histograma para los productos
    axes[1].bar(speciesList, productsDegree, color='orange', alpha=0.7)
    axes[1].set_title("Grado de Nodos - Productos")
    axes[1].set_xlabel("Especies")
    axes[1].set_ylabel("Grado")
    axes[1].tick_params(axis='x', rotation=90)

    # Ajustar diseño y mostrar los histogramas
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main('helium.chem')