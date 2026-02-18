def alphabeta(depth, alpha, beta, is_max):
    if depth == 0:
        return 1

    if is_max:
        value = -1000
        for _ in range(2):
            value = max(value, alphabeta(depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = 1000
        for _ in range(2):
            value = min(value, alphabeta(depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

print("Alpha-Beta Value:", alphabeta(3, -1000, 1000, True))
