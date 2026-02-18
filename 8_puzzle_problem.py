# 8-Puzzle Problem using A* Algorithm

from heapq import heappush, heappop

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Calculate number of misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Find position of blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all possible moves
def generate_moves(state):
    moves = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)

    return moves

# Convert list to tuple (for visited check)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search Algorithm
def solve_8_puzzle(start_state):
    pq = []
    heappush(pq, (heuristic(start_state), 0, start_state))
    visited = set()

    while pq:
        f, g, current = heappop(pq)

        if current == goal_state:
            print("Goal State Reached!")
            return

        visited.add(state_to_tuple(current))

        for move in generate_moves(current):
            if state_to_tuple(move) not in visited:
                h = heuristic(move)
                heappush(pq, (g + h, g + 1, move))

    print("Solution not found.")

# Input initial state
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solve_8_puzzle(start_state)
