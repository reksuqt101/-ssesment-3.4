
# Create Graph
def create_graph():
    graph = {
        "S": ["E", "L"],
        "E": ["S", "L2", "O"],
        "L": ["S", "T", "E2"],
        "L2": ["E"],
        "O": ["E"],
        "T": ["L"],
        "E2": ["L"]
    }

    return graph


# BFS
def bfs(graph, start):
    queue = [start]
    visited = []
    result = []

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            result.append(vertex[0])

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    result = [start[0]]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result += dfs(graph, neighbor, visited)

    return result


# Main Program
graph = create_graph()

print("GRAPH USING SELLOTE")
print("BFS:", " -> ".join(bfs(graph, "S")))
print("DFS:", " -> ".join(dfs(graph, "S")))
