"""utility.py file."""


def read_board(fname):
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
