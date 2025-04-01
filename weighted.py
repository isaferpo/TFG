import loki as lk
import matplotlib.pyplot as plt
import numpy as np

def main(file):
    # Parsear el archivo químico
    uniqueSpecies, reactions = lk.parseChemFile(file)

    # Inicializar matrices ponderadas como listas de diccionarios
    reactantsMatrix = []
    productsMatrix = []

    # Construcción de matrices ponderadas utilizando diccionarios
    for reaction in reactions:
        # Crear diccionarios para reactivos y productos
        reactantsRow = {species: 0 for species in uniqueSpecies}
        productsRow = {species: 0 for species in uniqueSpecies}

        # Marcar las especies en reactivos con sus coeficientes estequiométricos
        for species, coeff in zip(reaction['lhsSpecies'], reaction['lhsStoichiometricCoeffs']):
            reactantsRow[species] = coeff
            if reaction['backwardReaction']:
                productsRow[species] = coeff  # También marcar como producto

        # Marcar las especies en productos con sus coeficientes estequiométricos
        for species, coeff in zip(reaction['rhsSpecies'], reaction['rhsStoichiometricCoeffs']):
            productsRow[species] = coeff
            if reaction['backwardReaction']:
                reactantsRow[species] = coeff  # También marcar como reactivo

        # Convertir los diccionarios a listas y agregar a las matrices
        reactantsMatrix.append(list(reactantsRow.values()))
        productsMatrix.append(list(productsRow.values()))

    # Mostrar las matrices ponderadas con imshow antes de los histogramas
    mostrar_matriz_ponderada(reactantsMatrix, uniqueSpecies, "Matriz Ponderada de Reactivos")
    mostrar_matriz_ponderada(productsMatrix, uniqueSpecies, "Matriz Ponderada de Productos")

    reactants_matrix_w = np.save('reactantsMatrix.npy', reactantsMatrix)
    products_matrix_w = np.save('productsMatrix.npy', productsMatrix)

def mostrar_matriz_ponderada(matriz, speciesList, titulo):
    # Aumentamos el tamaño de la figura para que la cuadricula se vea más grande.
    plt.figure(figsize=(10, 6))
    # Usamos 'Blues' para representar valores ponderados y en particular que el 0 se vea blanco
    plt.imshow(matriz, cmap='Blues', interpolation='nearest', aspect='auto')
    plt.title(titulo)
    plt.xlabel("Especies")
    plt.ylabel("Reacciones")
    plt.xticks(range(len(speciesList)), speciesList, rotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main('helium.chem')