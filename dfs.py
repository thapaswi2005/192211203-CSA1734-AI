def dfs_recursive(graph, start, visited):
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs(graph, start):
    visited = set()
    dfs_recursive(graph, start, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting DFS from vertex 'A'
print("DFS starting from vertex 'A':")
dfs(graph, 'A')
