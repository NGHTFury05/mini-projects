
from collections import defaultdict
rmap=defaultdict(set)
cmap=defaultdict(set)
bmap=defaultdict(set)
import random
def generate_sudoku():
    base = 3
    side = base * base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    # remove some numbers to create the puzzle
    squares = side*side
    empties = squares * 3//4
    for p in random.sample(range(squares),empties):
        board[p//side][p%side] = 0

    return board
sudoku_grid = generate_sudoku()
def initialize_maps(grid):
    """Populate rmap, cmap, bmap from the initial grid."""
    rmap.clear(); cmap.clear(); bmap.clear()
    for r in range(9):
        for c in range(9):
            v = grid[r][c]
            if v != 0:
                bindex = (r // 3, c // 3)
                if v in rmap[r] or v in cmap[c] or v in bmap[bindex]:
                    raise ValueError(f"Invalid starting grid: duplicate {v} at {r},{c}")
                rmap[r].add(v)
                cmap[c].add(v)
                bmap[bindex].add(v)
initialize_maps(sudoku_grid)
def is_valid(row, col, num):
    bindex = (row // 3, col // 3)
    if num in rmap[row] or num in cmap[col] or num in bmap[bindex] :
        return False
    else:
        rmap[row].add(num)
        cmap[col].add(num)
        bmap[bindex].add(num)
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  
                for num in range(1, 10): 
                    if is_valid(row, col, num):
                        grid[row][col] = num  
                        if solve_sudoku(grid):  
                            return True
                        rmap[row].remove(num)
                        cmap[col].remove(num)
                        bindex = (row // 3, col // 3)
                        bmap[bindex].remove(num)
                        grid[row][col] = 0  
                return False  
    return True  
def print_board(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
solve_sudoku(sudoku_grid)
print_board(sudoku_grid)
# give a more visual nook to the sudoku board using libraries like matplotlib or seaborn
import matplotlib.pyplot as plt
import seaborn as sns
def plot_sudoku(grid):
    plt.figure(figsize=(6,6))
    sns.heatmap(grid, annot=True, cbar=False, linewidths=0.5, linecolor='black', 
                square=True, cmap='Blues', fmt='g', 
                annot_kws={"size": 16}, 
                mask=[[cell == 0 for cell in row] for row in grid])
    plt.xticks([])
    plt.yticks([])
    plt.title("Solved Sudoku", fontsize=20)
    plt.show()
plot_sudoku(sudoku_grid)












    