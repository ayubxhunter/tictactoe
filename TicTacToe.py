def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True
    return False

def tic_tac_toe():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    player = "X"
    print_board(board)
    while True:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))
        if board[row-1][col-1] != "-":
            print("Invalid move! That cell is already taken.")
            continue
        board[row-1][col-1] = player
        print_board(board)
        if check_win(board):
            print("Congratulations, player " + player + " wins!")
            break
        if all([cell != "-" for row in board for cell in row]):
            print("The game is a tie!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()
