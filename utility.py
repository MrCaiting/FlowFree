"""utility.py file."""
import itertools as itt
# Assign Binary values for each directions
UP = 0b0001         # decimal 1
DOWN = 0b0010       # decimal 2
LEFT = 0b0100       # decimal 4
RIGHT = 0b1000      # decimal 8

# Define all the possible movement on board with corresponding coordinate changes
MOVES = [(UP, 1, 0), (DOWN, -1, 0), (LEFT, 0, -1), (RIGHT, 0, 1)]


def read_board(file):
    """
    read_board.

    DESCRIPTION: utility function used to read the .txt board display file and
        to return the board in the format of an array and a dictionary of all
        the colors endpoints on board
    INPUTS:
        fname: The .txt file that we would like to read
    OUTPUTS:
        1. maze: an array that represents the parsed board
        2. all_colors: a dictionary of all colors that show up on board
    """
    colors = dict()     # create empty dictionary of colors
    file = file.read()
    board = file.splitlines()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell.isalpha():
                if cell in colors:
                    continue
                else:
                    color_index = len(colors)
                    colors[cell] = color_index
    return board, colors

def in_bound(i,j,width,height):
    #check if a cell in on board
    if i >= 0 and i < width and j >=0 and j < height:
        return True

def get_neighbors(i,j):
    #get all neighbors of a cell
    neighbors = []
    for (direction, x, y) in MOVES:
        neighbors.append((direction, i+x, j+y))
    return neighbors

def valid_neighbors(i,j,width,height):
    #check for neighbors that is in bound
    neighbors = []
    for (direction, x, y) in get_neighbors(i,j):
        if in_bound(x, y, width, height):
            neighbors.append((direction, x, y))
    return neighbors

def x_or(variables):
    #define function that performs logical XOR,
    # ie. returns list that any two of the
    # variables are different.
    xor_list = []
    combos = itt.combinations(variables,2)
    for (x, y) in combos:
        xor_list.append((-x, -y))
    return xor_list