"""utility.py file."""


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

    #create empty dictionary of colors
    colors = dict()
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