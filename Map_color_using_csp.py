def is_safe(region, color, assignment, adjacency):
    for neighbor in adjacency[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def map_coloring(regions, colors, adjacency, assignment):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if is_safe(region, color, assignment, adjacency):
            assignment[region] = color
            result = map_coloring(regions, colors, adjacency, assignment)
            if result:
                return result
            del assignment[region]

    return None


regions = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']
adjacency = {
    'A': ['B','C'],
    'B': ['A','C','D'],
    'C': ['A','B','D'],
    'D': ['B','C']
}

print(map_coloring(regions, colors, adjacency, {}))
