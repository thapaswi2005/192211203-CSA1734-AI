def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row):
    # base case: If all queens are placed
    if row >= len(board):
        return True

    # Consider this row and try placing this queen in all columns one by one
    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place this queen in board[row][col]
            board[row][col] = 1

            # Recur to place rest of the queens
            if solve_nqueens_util(board, row + 1):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, then remove queen
            board[row][col] = 0

    # If the queen cannot be placed in any column in this row, return False
    return False

def solve_nqueens():
    n = 8  # Number of queens
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

# Call the function to solve the 8 queens problem
solve_nqueens()
