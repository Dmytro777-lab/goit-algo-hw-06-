import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["Station 1", "Station 2", "Station 3"])
G.add_edges_from([("Station 1", "Station 2"), ("Station 2", "Station 3")])

nx.draw(G, with_labels=True)
plt.show()

nx.set_node_attributes(
    G, {"Station 1": {"type": "metro"}, "Station 2": {
        "type": "bus"}, "Station 3": {"type": "tram"}}, "info"
)
print("Node attributes:")
for node, attr in G.nodes(data=True):
    print(f"{node}: {attr}")

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(
    G) if nx.number_connected_components(G) == 1 else False

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Is the graph connected? {is_connected}")
