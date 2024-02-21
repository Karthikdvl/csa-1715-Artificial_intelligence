def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visited node: {start}")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

# Example graph represented as an adjacency list
graph = {
    '0': {'1', '2'},
    '1': {'0', '3', '4'},
    '2': {'0'},
    '3': {'1'},
    '4': {'2', '3'}
}

# Call DFS starting from node '0'
dfs(graph, '0')
