# 8-Queen Problem using Backtracking

N = 8

# Function to check if placing queen is safe
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function
def solve_queen(board, row):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queen(board, row + 1):
                return True
            board[row] = -1  # Backtrack

    return False

# Print the board
def print_solution(board):
    print("Solution:")
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Main
board = [-1] * N
solve_queen(board, 0)
