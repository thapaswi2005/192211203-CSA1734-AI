def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        player = players[turn % 2]
        print("Player {player}'s turn.")
        
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                if row < 0 or row > 2:
                    raise ValueError("Row must be between 0 and 2.")
                break
            except ValueError as e:
                print(e)
        
        while True:
            try:
                col = int(input("Enter column (0, 1, or 2): "))
                if col < 0 or col > 2:
                    raise ValueError("Column must be between 0 and 2.")
                break
            except ValueError as e:
                print(e)
        
        if board[row][col] != ' ':
            print("Invalid move. That space is already taken. Try again.")
            continue
        
        board[row][col] = player
        print_board(board)
        
        if check_win(board, player):
            print("Player {player} wins!")
            break
        
        if check_draw(board):
            print("It's a draw!")
            break
        
        turn += 1

# Run the game
tic_tac_toe()
