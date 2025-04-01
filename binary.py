import loki as lk
import matplotlib.pyplot as plt

def main(file):
    # Parsear el archivo químico
    uniqueSpecies, reactions = lk.parseChemFile(file)

    # Inicializar matrices binarias como listas de diccionarios
    reactantsMatrix = []
    productsMatrix = []

    # Construcción de matrices binarias utilizando diccionarios
    for reaction in reactions:
        # Crear diccionarios para reactivos y productos
        reactantsRow = {species: 0 for species in uniqueSpecies}
        productsRow = {species: 0 for species in uniqueSpecies}

        # Marcar las especies en reactivos y productos
        for species in reaction['lhsSpecies']:
            reactantsRow[species] = 1
            if reaction['backwardReaction']:
                productsRow[species] = 1  # También marcar como producto

        for species in reaction['rhsSpecies']:
            productsRow[species] = 1
            if reaction['backwardReaction']:
                reactantsRow[species] = 1  # También marcar como reactivo

        # Convertir los diccionarios a listas y agregar a las matrices
        reactantsMatrix.append(list(reactantsRow.values()))
        productsMatrix.append(list(productsRow.values()))

    # Mostrar las matrices binarias con imshow antes de los histogramas
    mostrar_matriz_binaria(reactantsMatrix, uniqueSpecies, "Matriz binaria de Reactivos")
    mostrar_matriz_binaria(productsMatrix, uniqueSpecies, "Matriz binaria de Productos")

    # Calcular el grado de los nodos para las especies (suma de cada columna)
    reactantsDegree = [sum(col) for col in zip(*reactantsMatrix)]
    productsDegree = [sum(col) for col in zip(*productsMatrix)]

    # Crear histogramas del grado de los nodos
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Histograma para los reactivos
    axes[0].bar(uniqueSpecies, reactantsDegree, color='blue', alpha=0.7)
    axes[0].set_title("Grado de Nodos - Reactivos")
    axes[0].set_xlabel("Especies")
    axes[0].set_ylabel("Grado")
    axes[0].tick_params(axis='x', rotation=90)

    # Histograma para los productos
    axes[1].bar(uniqueSpecies, productsDegree, color='orange', alpha=0.7)
    axes[1].set_title("Grado de Nodos - Productos")
    axes[1].set_xlabel("Especies")
    axes[1].set_ylabel("Grado")
    axes[1].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    plt.show()


def mostrar_matriz_binaria(matriz, speciesList, titulo):
    # Aumentamos el tamaño de la figura para que la cuadricula se vea más grande.
    plt.figure(figsize=(10, 6))
    # Usamos 'binary' para que el valor 1 se muestre en negro y 0 en blanco
    plt.imshow(matriz, cmap='binary', interpolation='nearest', aspect='auto')
    plt.title(titulo)
    plt.xlabel("Especies")
    plt.ylabel("Reacciones")
    plt.xticks(range(len(speciesList)), speciesList, rotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main('helium.chem')