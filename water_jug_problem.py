# Water Jug Problem using BFS

from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque()

    # (jug1, jug2)
    queue.append((0, 0))

    while queue:
        j1, j2 = queue.popleft()

        # Goal check
        if j1 == target or j2 == target:
            print("Goal Reached:", (j1, j2))
            return

        if (j1, j2) in visited:
            continue

        visited.add((j1, j2))
        print((j1, j2))

        # All possible operations
        states = [
            (cap1, j2),               # Fill jug1
            (j1, cap2),               # Fill jug2
            (0, j2),                  # Empty jug1
            (j1, 0),                  # Empty jug2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),  # Pour jug1 → jug2
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))   # Pour jug2 → jug1
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible.")

# Main
water_jug(4, 3, 2)
