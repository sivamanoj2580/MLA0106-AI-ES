# Vacuum Cleaner Problem (Two-Room Environment)

def vacuum_cleaner(location, state):
    print("Initial State:")
    print("Location:", location, "State:", state)

    # If current room is dirty, clean it
    if state[location] == 1:
        print("Action: Suck")
        state[location] = 0

    # Move to the other room
    if location == 0:
        print("Action: Move Right")
        location = 1
    else:
        print("Action: Move Left")
        location = 0

    # Clean the other room if dirty
    if state[location] == 1:
        print("Action: Suck")
        state[location] = 0

    print("Final State:")
    print("Location:", location, "State:", state)

# Main
# 0 = Room A, 1 = Room B
# 1 = Dirty, 0 = Clean
vacuum_cleaner(0, [1, 1])
        