"""utility.py file."""
from functools import reduce
import itertools as itt

# Some useful majic numbers
PAIR = 2

# Assign binary values for each directions
UP = 4         # decimal 1
DOWN = 8       # decimal 2
LEFT = 1       # decimal 4
RIGHT = 2      # decimal 8

# Assign binary values for the direction for each flow
UPDOWN = UP | DOWN
LRIGHT = LEFT | RIGHT
UPRIGHT = UP | RIGHT
UPLEFT = UP | LEFT
DRIGHT = DOWN | RIGHT
DLEFT = DOWN | LEFT

# Define all the possible movement on board with corresponding coordinate changes
MOVES = [(LEFT, 0, -1), (RIGHT, 0, 1), (UP, -1, 0), (DOWN, 1, 0)]

# Define all the possible flow direction structures
FLOWDIR = [LRIGHT, UPDOWN,
           UPLEFT, UPRIGHT,
           DLEFT, DRIGHT]
# FLOWDIR = [UPDOWN, LRIGHT,
#           UPRIGHT, UPLEFT,
#           DRIGHT, DLEFT]

# ANSI_CODES
COLOR_ANSI = dict(B=104, R=101, G=42, Y=103, O=43)
ANSI_RESET = '\033[0m'
ANSI_FORMAT = '\033[30;{}m'


def read_board(file):
    """read_board.

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


def in_bound(i, j, width, height):
    """in_bound.

    DESCRIPTION: check if a cell in on board
    """
    if i >= 0 and i < width and j >= 0 and j < height:
        return True


def get_neighbors(i, j):
    """get_neighbors.

    DESCRIPTION: get all neighbors of a cell
    """
    neighbors = []
    for (direction, x, y) in MOVES:
        neighbors.append((direction, i+x, j+y))
    return neighbors


def valid_neighbors(i, j, width, height):
    """valid_neighbors.

    DESCRIPTION: check for neighbors that is in bound
    """
    neighbors = []
    for (direction, x, y) in get_neighbors(i, j):
        if in_bound(x, y, width, height):
            neighbors.append((direction, x, y))
    return neighbors


def x_or(variables):
    """x_or.

    DESCRIPTION: Define function that performs logical XOR,
        ie. returns list that any two of the
        variables are different
    INPUTS:
        variables: a list of all SAT variables we'd like to compute
    OUTPUTS:
        xor_list: the result as a list
    """
    xor_list = []
    combos = itt.combinations(variables, PAIR)
    for (x, y) in combos:
        xor_list.append([-x, -y])
    return xor_list


def or_seq(sequence):
    """or_seq.

    DESCRIPTION: Helper function to get the input as an interable sequence and
        apply bitwise OR one each pair of elements in order
    INPUTS:
        sequence: an iterable sequence
    OUTPUTS:
        result: the result after applying OR
    """
    result = reduce(lambda x, y: x | y, sequence, 0)
    return result
