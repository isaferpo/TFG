import os
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Definir la ruta base
base_path = os.path.dirname(os.path.abspath(__file__))

# Crear un grafo bipartito
B = nx.Graph()

# Leer nodos del conjunto A
nodos_especies_path = os.path.join(base_path, 'nodos_especies.txt')
with open(nodos_especies_path, 'r') as file:
    nodos_especies = {line.strip() for line in file}
    B.add_nodes_from(nodos_especies, bipartite=0)  # Etiquetar como parte del conjunto 0

# Leer nodos del conjunto B
nodos_reacciones_path = os.path.join(base_path, 'nodos_reacciones.txt')
with open(nodos_reacciones_path, 'r') as file:
    nodos_reacciones = {line.strip() for line in file}
    B.add_nodes_from(nodos_reacciones, bipartite=1)  # Etiquetar como parte del conjunto 1

# Leer las aristas desde el archivo
edges_path = os.path.join(base_path, 'edges_helium.txt')
with open(edges_path, 'r') as file:
    edges = [tuple(line.strip().split()) for line in file]
    B.add_edges_from(edges)

# Verificar la estructura de la red
print("Nodos en el conjunto A:", list(nodos_especies))
print("Nodos en el conjunto B:", list(nodos_reacciones))
print("Número de nodos:", B.number_of_nodes())
print("Número de aristas:", B.number_of_edges())

# Posicionamiento de los nodos
pos = nx.bipartite_layout(B, nodos_especies)  # Usa los nodos de A para la disposición

# Dibujar la red bipartita
plt.figure(figsize=(8, 6))
nx.draw(B, pos, with_labels=True, node_size=700, 
        node_color=["red" if n in nodos_especies else "blue" for n in B.nodes()], 
        edge_color="gray", font_size=10)
plt.title("Red Bipartita")
plt.show()

# Construir la matriz de adyacencia

Amat = nx.to_pandas_adjacency(B)
Amat.to_csv(os.path.join(base_path, 'matriz_adyacencia_helium.csv'), index=True, header=True)
print(Amat)