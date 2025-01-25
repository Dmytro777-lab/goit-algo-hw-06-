import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_weighted_edges_from([
    ("Station 1", "Station 2", 4),
    ("Station 2", "Station 3", 3),
    ("Station 3", "Station 4", 2),
    ("Station 4", "Station 5", 7),
    ("Station 5", "Station 1", 10),
    ("Station 2", "Station 4", 1)
])


def dijkstra_shortest_path(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min((node for node in graph.nodes if node not in visited),
                           key=lambda node: shortest_paths[node])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = shortest_paths[current_node] + weight
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance

    return shortest_paths


shortest_paths_from_station1 = dijkstra_shortest_path(G, "Station 1")
print("Shortest paths from Station 1:", shortest_paths_from_station1)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        font_weight='bold', edge_color='gray', width=1, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
