import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(f"{vertex} ", end="")

        # Add unvisited neighbors to the queue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    # Example graph (adjacency list representation)
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [2],
        4: [0]
    }

    print("Breadth-First Traversal:")
    bfs(graph, 0)
