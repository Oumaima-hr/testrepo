import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(num_vertices, num_edges):
    """Génère un graphe orienté avec des distances aléatoires."""
    graph = []
    edges_set = set()
    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        while v == u or (u, v) in edges_set:  # Évite les boucles et les doublons
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 20)  # Poids aléatoire entre 1 et 20
        graph.append((u, v, weight))
        edges_set.add((u, v))
    return graph

def draw_graph(num_vertices, edges):
    """Trace le graphe généré."""
    G = nx.DiGraph()
    G.add_nodes_from(range(num_vertices))
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)  # Positionne les nœuds
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graphe généré")
    plt.show()

def bellman_ford(num_vertices, edges, start):
    """Implémente l'algorithme de Bellman-Ford."""
    # Initialisation des distances
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Étape 1 : Relaxation des arêtes
    for i in range(num_vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Étape 2 : Détection de cycles négatifs
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Le graphe contient un cycle de poids négatif.")
            return None

    return distances

def main():
    print("\nAlgorithme de Bellman-Ford")
    num_vertices = int(input("Entrez le nombre de sommets : "))
    num_edges = int(input("Entrez le nombre d'arêtes : "))

    # Génération aléatoire du graphe
    graph = generate_graph(num_vertices, num_edges)
    print("\nGraphe généré (arêtes avec poids) :")
    for u, v, weight in graph:
        print(f"{u} -> {v} (poids : {weight})")

    # Visualisation du graphe
    draw_graph(num_vertices, graph)

    start = int(input("\nEntrez le sommet de départ (0 à {}): ".format(num_vertices - 1)))

    # Exécution de Bellman-Ford
    distances = bellman_ford(num_vertices, graph, start)
    if distances is not None:
        print("\nDistances minimales depuis le sommet {} :".format(start))
        for i, d in enumerate(distances):
            print(f"Distance vers {i} : {d}")

if __name__ == "__main__":
    main()
