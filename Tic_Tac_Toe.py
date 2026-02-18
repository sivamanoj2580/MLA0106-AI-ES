board = [' ']*9

def show():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in w) for w in wins)

player = 'X'
for _ in range(9):
    show()
    pos = int(input(f"Player {player} (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = player
        if winner(player):
            show()
            print("Winner:", player)
            break
        player = 'O' if player == 'X' else 'X'
else:
    show()
    print("Draw")
