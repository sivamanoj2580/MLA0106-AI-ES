# Missionaries and Cannibals Problem using BFS

from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if (m_left > 0 and c_left > m_left):
        return False

    if (m_right > 0 and c_right > m_right):
        return False

    return True

def missionaries_cannibals():
    start = (3, 3, 0)   # (M_left, C_left, Boat_position 0=Left,1=Right)
    goal = (0, 0, 1)

    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    while queue:
        state = queue.popleft()
        m_left, c_left, boat = state

        if state == goal:
            print("Goal Reached!")
            return

        if boat == 0:  # Boat on left
            moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
            for m, c in moves:
                new_state = (m_left - m, c_left - c, 1)
                if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
                    print(state, "->", new_state)

        else:  # Boat on right
            moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
            for m, c in moves:
                new_state = (m_left + m, c_left + c, 0)
                if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
                    print(state, "->", new_state)

# Main
missionaries_cannibals()
