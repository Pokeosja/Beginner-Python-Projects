"""
🧩 SUDOKU SOLVER
🔢 Created by: Raveem Osja
✨ Solves any valid Sudoku puzzle
"""

def print_sudoku(board):
    """Display Sudoku board beautifully"""
    print("\n" + "=" * 37)
    print("          🧩 SUDOKU BOARD 🧩")
    print("=" * 37)
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("  " + "-" * 35)
        
        row = []
        for j in range(9):
            if j % 3 == 0:
                row.append(" │ ")
            row.append(f" {board[i][j] if board[i][j] != 0 else '·'} ")
        
        row.append(" │ ")
        print("".join(row))
    
    print("=" * 37)

def is_valid(board, row, col, num):
    """Check if a number can be placed at board[row][col]"""
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty(board):
    """Find an empty cell (0) in the board"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board, step_by_step=False):
    """Solve Sudoku using backtracking"""
    empty = find_empty(board)
    
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if step_by_step:
                print(f"\n📝 Placing {num} at ({row+1}, {col+1})")
                print_sudoku(board)
                input("⏭️ Press Enter to continue...")
            
            if solve_sudoku(board, step_by_step):
                return True
            
            # Backtrack
            board[row][col] = 0
            
            if step_by_step:
                print(f"\n↩️ Backtracking from ({row+1}, {col+1})")
                print_sudoku(board)
                input("⏭️ Press Enter to continue...")
    
    return False

def sudoku_solver():
    print("=" * 50)
    print("🧩  SUDOKU SOLVER & CHECKER  🧩")
    print("=" * 50)
    
    print("\n📝 Choose an option:")
    print("1. 🎮 Solve a sample puzzle")
    print("2. ✍️ Enter your own puzzle")
    print("3. ✅ Check if a puzzle is valid")
    
    choice = input("\n🎯 Enter choice (1-3): ")
    
    if choice == '1':
        # Sample puzzle (0 represents empty cells)
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        print("\n📊 Sample Puzzle:")
        print_sudoku(puzzle)
        
        step_by_step = input("\n🔍 Show solving steps? (yes/no): ").lower() == 'yes'
        
        print("\n" + "=" * 30)
        print("🧠 SOLVING PUZZLE...")
        print("=" * 30)
        
        if solve_sudoku(puzzle, step_by_step):
            print("\n✅ PUZZLE SOLVED!")
            print_sudoku(puzzle)
        else:
            print("\n❌ No solution exists!")
    
    elif choice == '2':
        print("\n📝 Enter your Sudoku puzzle row by row")
        print("   Use 0 for empty cells, separate with spaces")
        
        puzzle = []
        for i in range(9):
            while True:
                row_input = input(f"Row {i+1}: ")
                try:
                    row = list(map(int, row_input.split()))
                    if len(row) == 9 and all(0 <= x <= 9 for x in row):
                        puzzle.append(row)
                        break
                    else:
                        print("❌ Please enter exactly 9 numbers (0-9)")
                except:
                    print("❌ Invalid input!")
        
        print("\n📊 Your Puzzle:")
        print_sudoku(puzzle)
        
        if solve_sudoku(puzzle):
            print("\n✅ SOLUTION FOUND!")
            print_sudoku(puzzle)
        else:
            print("\n❌ No solution exists!")
    
    elif choice == '3':
        print("\n🔍 Sudoku Validator")
        print("📝 Enter a complete Sudoku puzzle to check")
        
        puzzle = []
        for i in range(9):
            while True:
                row_input = input(f"Row {i+1}: ")
                try:
                    row = list(map(int, row_input.split()))
                    if len(row) == 9 and all(1 <= x <= 9 for x in row):
                        puzzle.append(row)
                        break
                    else:
                        print("❌ Please enter exactly 9 numbers (1-9)")
                except:
                    print("❌ Invalid input!")
        
        # Check if valid
        is_valid_puzzle = True
        
        # Check rows and columns
        for i in range(9):
            if len(set(puzzle[i])) != 9:
                is_valid_puzzle = False
                break
            
            column = [puzzle[j][i] for j in range(9)]
            if len(set(column)) != 9:
                is_valid_puzzle = False
                break
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(puzzle[box_row + i][box_col + j])
                
                if len(set(box)) != 9:
                    is_valid_puzzle = False
                    break
        
        print("\n" + "=" * 30)
        print_sudoku(puzzle)
        if is_valid_puzzle:
            print("✅ VALID SUDOKU PUZZLE!")
        else:
            print("❌ INVALID SUDOKU PUZZLE!")
    
    # Run again
    if input("\n🔄 Run again? (yes/no): ").lower() == 'yes':
        sudoku_solver()

if __name__ == "__main__":
    sudoku_solver()