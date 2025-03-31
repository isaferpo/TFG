import loki as lk
import matplotlib.pyplot as plt

def main(file):
    # Parsear el archivo químico
    uniqueSpecies, reactions = lk.parseChemFile(file)

    # Lista ordenada de especies únicas
    speciesList = sorted(uniqueSpecies)

    # Inicializar matrices binarias
    reactantsMatrix = []
    productsMatrix = []

    # Construcción usando sets y comprensión de listas
    for reaction in reactions:
        lhs_species = set(reaction['lhsSpecies'])  # Reactivos
        rhs_species = set(reaction['rhsSpecies'])    # Productos

        reactantsRow = [1 if species in lhs_species else 0 for species in speciesList]
        productsRow  = [1 if species in rhs_species else 0 for species in speciesList]

        reactantsMatrix.append(reactantsRow)
        productsMatrix.append(productsRow)

    # Mostrar las cuadriculas (matrices binarias) con imshow antes de los histogramas
    mostrar_matriz_binaria(reactantsMatrix, speciesList, "Matriz binaria de Reactivos")
    mostrar_matriz_binaria(productsMatrix, speciesList, "Matriz binaria de Productos")

    # Calcular el grado de los nodos para las especies (suma de cada columna)
    reactantsDegree = [sum(col) for col in zip(*reactantsMatrix)]
    productsDegree = [sum(col) for col in zip(*productsMatrix)]

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

    plt.tight_layout()
    plt.show()


def mostrar_matriz_binaria(matriz, speciesList, titulo):
    # Aumentamos el tamaño de la figura para que la cuadricula se vea más grande.
    plt.figure(figsize=(20, 12))
    # Usamos 'gray_r' para que el valor 1 se muestre en negro y 0 en blanco
    plt.imshow(matriz, cmap='gray_r', interpolation='nearest')
    plt.title(titulo)
    plt.xlabel("Especies")
    plt.ylabel("Reacciones")
    plt.xticks(range(len(speciesList)), speciesList, rotation=90)
    plt.yticks(range(len(matriz)))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main('helium.chem')