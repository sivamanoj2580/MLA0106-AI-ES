def a_star(graph, heuristic, start, goal):
    open_set = {start}
    g = {start: 0}
    parent = {start: None}

    while open_set:
        current = min(open_set, key=lambda x: g[x] + heuristic[x])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_set.remove(current)

        for neighbor, cost in graph[current]:
            new_cost = g[current] + cost
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                parent[neighbor] = current
                open_set.add(neighbor)

    return None


graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',2)],
    'C': [('D',1)],
    'D': []
}

heuristic = {'A':4, 'B':2, 'C':1, 'D':0}

print("Path:", a_star(graph, heuristic, 'A', 'D'))
