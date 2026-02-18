def minimax(depth, is_max):
    if depth == 0:
        return 1

    if is_max:
        return max(minimax(depth-1, False), minimax(depth-1, False))
    else:
        return min(minimax(depth-1, True), minimax(depth-1, True))

print("Minimax Value:", minimax(3, True))
