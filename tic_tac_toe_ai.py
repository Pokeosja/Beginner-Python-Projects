"""
❌⭕ TIC TAC TOE WITH AI
🤖 Created by: Raveem Osja
⚡ Play against a basic AI opponent
"""

import random

def print_board(board):
    """Display the game board"""
    print("\n" + "=" * 25)
    print("     TIC TAC TOE")
    print("=" * 25)
    
    for i in range(3):
        row_display = []
        for j in range(3):
            if board[i][j] == 'X':
                row_display.append("❌")
            elif board[i][j] == 'O':
                row_display.append("⭕")
            else:
                row_display.append("⬜")
        
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

def get_empty_positions(board):
    """Get all empty positions"""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def ai_move(board):
    """Basic AI that tries to win or block"""
    # Try to win
    for i, j in get_empty_positions(board):
        board[i][j] = 'O'
        if check_winner(board, 'O'):
            board[i][j] = ' '
            return i, j
        board[i][j] = ' '
    
    # Try to block player
    for i, j in get_empty_positions(board):
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            board[i][j] = ' '
            return i, j
        board[i][j] = ' '
    
    # Try to take center
    if board[1][1] == ' ':
        return 1, 1
    
    # Try to take corners
    corners = [(0,0), (0,2), (2,0), (2,2)]
    empty_corners = [pos for pos in corners if board[pos[0]][pos[1]] == ' ']
    if empty_corners:
        return random.choice(empty_corners)
    
    # Random move
    return random.choice(get_empty_positions(board))

def tic_tac_toe_ai():
    print("=" * 50)
    print("🤖  TIC TAC TOE - YOU VS AI  🤖")
    print("=" * 50)
    print("\n🎮 You: ❌  |  AI: ⭕")
    print("📝 Enter row and column (1-3) for your move\n")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for player, False for AI
    
    while True:
        print_board(board)
        
        if player_turn:
            print("\n🎯 Your turn (❌)")
            try:
                row = int(input("📍 Enter row (1-3): ")) - 1
                col = int(input("📍 Enter column (1-3): ")) - 1
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("❌ Please enter numbers between 1 and 3!")
                    continue
                
                if board[row][col] != ' ':
                    print("❌ That position is already taken!")
                    continue
                
                board[row][col] = 'X'
                
                if check_winner(board, 'X'):
                    print_board(board)
                    print("\n" + "=" * 30)
                    print("🎉 YOU WIN! 🎉")
                    print("=" * 30)
                    break
                
                player_turn = False
                
            except ValueError:
                print("❌ Please enter valid numbers!")
        
        else:
            print("\n🤖 AI's turn (⭕)...")
            row, col = ai_move(board)
            board[row][col] = 'O'
            print(f"🤖 AI placed at position ({row+1}, {col+1})")
            
            if check_winner(board, 'O'):
                print_board(board)
                print("\n" + "=" * 30)
                print("💀 AI WINS! 💀")
                print("=" * 30)
                break
            
            player_turn = True
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("\n" + "=" * 30)
            print("🤝 IT'S A TIE! 🤝")
            print("=" * 30)
            break
    
    # Play again option
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        tic_tac_toe_ai()

if __name__ == "__main__":
    tic_tac_toe_ai()