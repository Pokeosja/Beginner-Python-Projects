"""
❌⭕ TIC TAC TOE - TWO PLAYER
👥 Created by: Raveem Osja
🎮 Classic two-player terminal game
"""

def print_board(board):
    """Display the game board with emojis"""
    print("\n" + "=" * 25)
    print("     TIC TAC TOE BOARD")
    print("=" * 25)
    
    for i in range(3):
        row_display = []
        for j in range(3):
            if board[i][j] == 'X':
                row_display.append("❌")
            elif board[i][j] == 'O':
                row_display.append("⭕")
            else:
                row_display.append(f"{(i*3 + j + 1)}")
        
        print("     " + " | ".join(row_display))
        if i < 2:
            print("     " + "---" * 5)

def check_winner(board, player):
    """Check if the current player has won"""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full"""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    print("=" * 50)
    print("❌⭕  TIC TAC TOE - TWO PLAYERS  ❌⭕")
    print("=" * 50)
    print("\n🎮 Player 1: ❌  |  Player 2: ⭕")
    print("📝 Enter numbers 1-9 to place your mark\n")
    
    # Initialize board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    player_names = {'X': "Player 1 (❌)", 'O': "Player 2 (⭕)"}
    
    while True:
        print_board(board)
        print(f"\n🎯 {player_names[current_player]}'s turn")
        
        try:
            move = int(input("📍 Enter position (1-9): "))
            
            if move < 1 or move > 9:
                print("❌ Please enter a number between 1 and 9!")
                continue
            
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if board[row][col] != ' ':
                print("❌ That position is already taken!")
                continue
            
            # Make the move
            board[row][col] = current_player
            
            # Check for winner
            if check_winner(board, current_player):
                print_board(board)
                print("\n" + "=" * 30)
                print(f"🎉 {player_names[current_player]} WINS! 🎉")
                print("=" * 30)
                break
            
            # Check for tie
            if is_board_full(board):
                print_board(board)
                print("\n" + "=" * 30)
                print("🤝 IT'S A TIE! 🤝")
                print("=" * 30)
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Play again option
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()