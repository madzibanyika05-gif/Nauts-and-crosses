def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board):
    # Check rows, columns and diagonals
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    for col in range(len(board)):
        if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(len(board))):
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]

    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]

    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("Cell already taken! Choose another.")

if __name__ == "__main__":
    tic_tac_toe()
