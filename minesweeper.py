"""
💣 MINESWEEPER GAME
🎮 Created by: Raveem Osja
🚩 Classic minesweeper in CLI
"""

import random

def create_board(size=8, mines=10):
    """Create a minesweeper board"""
    board = [[0 for _ in range(size)] for _ in range(size)]
    display = [['⬜' for _ in range(size)] for _ in range(size)]
    
    # Place mines
    mines_placed = 0
    while mines_placed < mines:
        row = random.randint(0, size-1)
        col = random.randint(0, size-1)
        
        if board[row][col] != 'M':
            board[row][col] = 'M'
            mines_placed += 1
            
            # Update numbers around mine
            for i in range(max(0, row-1), min(size, row+2)):
                for j in range(max(0, col-1), min(size, col+2)):
                    if board[i][j] != 'M':
                        board[i][j] += 1
    
    return board, display

def print_board(display, show_all=False):
    """Print the game board"""
    size = len(display)
    
    print("\n" + "=" * (size*3 + 4))
    print("    💣 MINESWEEPER 💣")
    print("=" * (size*3 + 4))
    
    # Column numbers
    print("   " + " ".join(f"{i+1:2}" for i in range(size)))
    print("  " + "---" * size)
    
    # Board with row numbers
    for i in range(size):
        row_display = []
        for j in range(size):
            if show_all and isinstance(display[i][j], int):
                if display[i][j] == 0:
                    row_display.append("  ")
                else:
                    row_display.append(f"{display[i][j]} ")
            elif display[i][j] == 'M':
                row_display.append("💣")
            elif display[i][j] == 'F':
                row_display.append("🚩")
            elif display[i][j] == '⬜':
                row_display.append("⬜")
            else:
                row_display.append(f"{display[i][j]} ")
        
        print(f"{i+1:2}| " + " ".join(row_display))
    
    print("=" * (size*3 + 4))

def reveal_cells(board, display, row, col, visited):
    """Reveal cells recursively for empty spaces"""
    size = len(board)
    
    if (row, col) in visited:
        return
    visited.add((row, col))
    
    if board[row][col] == 0:
        display[row][col] = '  '
        # Reveal adjacent cells
        for i in range(max(0, row-1), min(size, row+2)):
            for j in range(max(0, col-1), min(size, col+2)):
                if (i, j) != (row, col):
                    reveal_cells(board, display, i, j, visited)
    else:
        display[row][col] = board[row][col]

def minesweeper():
    print("=" * 50)
    print("💣  MINESWEEPER GAME  💣")
    print("=" * 50)
    
    size = 8
    mines = 10
    board, display = create_board(size, mines)
    flags = mines
    game_over = False
    revealed = 0
    
    print(f"\n🎮 Board: {size}x{size}")
    print(f"💣 Mines: {mines}")
    print(f"🚩 Flags available: {flags}")
    print("\n📝 Commands:")
    print("  R row col - Reveal a cell")
    print("  F row col - Place/remove flag")
    print("  Q - Quit game")
    
    while not game_over:
        print_board(display)
        print(f"\n🚩 Flags: {flags}")
        
        try:
            command = input("\n🎮 Enter command (R/F/Q): ").upper().split()
            
            if command[0] == 'Q':
                print("\n👋 Thanks for playing!")
                break
            
            if len(command) != 3:
                print("❌ Invalid command format!")
                continue
            
            action, row, col = command[0], int(command[1])-1, int(command[2])-1
            
            if not (0 <= row < size and 0 <= col < size):
                print("❌ Invalid coordinates!")
                continue
            
            if action == 'F':
                # Toggle flag
                if display[row][col] == '⬜':
                    if flags > 0:
                        display[row][col] = 'F'
                        flags -= 1
                    else:
                        print("❌ No flags remaining!")
                elif display[row][col] == 'F':
                    display[row][col] = '⬜'
                    flags += 1
                else:
                    print("❌ Cannot flag revealed cell!")
            
            elif action == 'R':
                if display[row][col] == 'F':
                    print("❌ Remove flag first!")
                    continue
                
                if board[row][col] == 'M':
                    print("\n" + "=" * 30)
                    print("💥 BOOM! YOU HIT A MINE! 💥")
                    print("=" * 30)
                    print_board(board, show_all=True)
                    game_over = True
                else:
                    if display[row][col] == '⬜':
                        visited = set()
                        reveal_cells(board, display, row, col, visited)
                        revealed += len([1 for i in range(size) for j in range(size) 
                                       if display[i][j] != '⬜' and display[i][j] != 'F'])
                    
                    # Check win condition
                    if revealed == size*size - mines:
                        print("\n" + "=" * 30)
                        print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                        print("=" * 30)
                        print_board(board, show_all=True)
                        game_over = True
            
            else:
                print("❌ Invalid command!")
                
        except (ValueError, IndexError):
            print("❌ Invalid input!")
    
    # Play again option
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        minesweeper()

if __name__ == "__main__":
    minesweeper()