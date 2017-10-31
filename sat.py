"""sat file converting problem to sat."""

from cnf import get_dir_var, form_color_cnf, get_cell_cIndex, form_dir_cnf
import time
import sys
from utility import ANSI_RESET, ANSI_FORMAT, COLOR_ANSI


def sat(board, colors):
    """sat.

    DESCRIPTION: reduce the board to SAT problem in conjunctive normal form
    INPUT:
        board: Game board
        colors: dictionary of colors
    OUTPUT:
        dvars: direction variables
        num_vars: total number of variables
        cnf: complete CNF
        t: time of reducing to SAT
    """
    num_colors = len(colors)
    # get dimensions of the board
    width = len(board[0])
    height = len(board)

    num_cells = width * height
    num_cvars = num_cells * num_colors

    # start clocking
    start = time.clock()

    # CNF of directions
    d_sat_var, num_dvars = get_dir_var(board, num_cvars)
    dir_clauses = form_dir_cnf(board, colors, d_sat_var)

    # CNF of colors
    col_clauses = form_color_cnf(board, colors)

    # end time
    t = time.clock() - start

    # calculate the total number of variables
    num_vars = num_cvars + num_dvars

    # get total CNF
    clauses = col_clauses + dir_clauses
    print("CNF: ", clauses)
    # print("d_sat_var:", d_sat_var)
    return d_sat_var, num_vars, clauses, t


def decode(board, colors, path):
    """decode.

    DESCRIPTION: convert back from solved sat to readable solutions.
    INPUT:
        board: Game board
        colors: dictionary of colors
        path: solution path of the Game
    OUTPUT:
        converted: a converted understandable list of the solution path.
    """
    pathCP = []
    # converted passed in path into a list of int
    for element in path:
        pathCP.append(int(element))

    # make a set of solution path
    path = set(pathCP)
    converted = []

    width = len(board[0])
    # height = len(board)

    # get direction variables
    dvar, _ = get_dir_var(board, len(colors))
    for i, row in enumerate(board):
        # for each row create empty array
        rows = []
        for j, cell in enumerate(row):

            curr_cell_color = -1

            for c in range(len(colors)):
                if get_cell_cIndex(width, i, j, colors, c) in path:
                    curr_cell_color = c

            curr_cell_direction = -1

            if not cell.isalpha():
                for direction, value in dvar[i, j].items():
                    if value in path:
                        curr_cell_direction = direction
            rows.append((curr_cell_color, curr_cell_direction))
        converted.append(rows)

    return converted


def visualize(converted, colors, mode_enable):
    """visualize.

    DESCRIPTION: visualize the decoded solution
    INPUT: converted: decoded solutions
            colors: color dictionary
    """
    # get the keys of colors dictionary
    # list of NONEs ready for assigning colors
    color_keys = len(colors)*[None]

    for key, color in colors.items():
        color_keys[color] = key
        # if color mode is enabled
        paint = mode_enable and key in COLOR_ANSI

    for row in converted:
        for (c, d) in row:
            color_cell = color_keys[c]

            display_cell = color_cell
            # for cells that are not endpoints
            if paint:
                if color_cell in COLOR_ANSI:
                    ansi = ANSI_FORMAT.format(COLOR_ANSI[color_cell])
                else:
                    ansi = ANSI_RESET

                sys.stdout.write(ansi)
            sys.stdout.write(display_cell)

        if mode_enable:
            sys.stdout.write(ANSI_RESET)

        sys.stdout.write('\n')
