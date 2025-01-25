import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(
    ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"])
G.add_edges_from([("Station 1", "Station 2"), ("Station 2", "Station 3"),
                  ("Station 3", "Station 4"), ("Station 4", "Station 5"),
                  ("Station 5", "Station 1"), ("Station 2", "Station 4")])


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None


dfs_result = dfs_path(G, "Station 1", "Station 5")
bfs_result = bfs_path(G, "Station 1", "Station 5")

print("DFS Path:", dfs_result)
print("BFS Path:", bfs_result)
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()
