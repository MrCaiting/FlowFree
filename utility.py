"""utility.py file."""

# Assign Binary values for each directions
UP = 0b0001         # decimal 1
DOWN = 0b0010       # decimal 2
LEFT = 0b0100       # decimal 4
RIGHT = 0b1000      # decimal 8

# Define all the possible movement on board with corresponding coordinate changes
movements = [(UP, 1, 0), (DOWN, -1, 0), (LEFT, 0, -1), (RIGHT, 0, 1)]


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
