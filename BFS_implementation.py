# Breadth First Search (BFS) implementation

from collections import deque

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque()          # Queue for BFS

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Main
bfs(graph, 'A')
