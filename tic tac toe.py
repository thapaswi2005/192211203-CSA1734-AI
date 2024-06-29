import math

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Initialize the board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check if there are any moves left
def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

# Evaluate the board
def evaluate(board):
    # Check rows, columns and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == PLAYER_X else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == PLAYER_X else -10

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER_X else -10

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER_X else -10

    return 0

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Find the best move for the current player
def find_best_move(board, is_maximizing):
    best_val = -math.inf if is_maximizing else math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X if is_maximizing else PLAYER_O
                move_val = minimax(board, 0, not is_maximizing, -math.inf, math.inf)
                board[i][j] = EMPTY
                if is_maximizing and move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
                elif not is_maximizing and move_val < best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Main game loop
def play_game():
    board = create_board()
    current_player = PLAYER_X
    print("Initial board:")
    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        if current_player == PLAYER_X:
            print("Player X's turn:")
            x, y = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[x][y] == EMPTY:
                board[x][y] = PLAYER_X
                current_player = PLAYER_O
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn:")
            move = find_best_move(board, False)
            board[move[0]][move[1]] = PLAYER_O
            current_player = PLAYER_X

        print_board(board)

    score = evaluate(board)
    if score == 10:
        print("Player X wins!")
    elif score == -10:
        print("Player O wins!")
    else:
        print("It's a draw!")

# Start the game
play_game()
