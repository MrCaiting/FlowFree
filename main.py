"""main function running the whole puzzle solver."""

from utility import read_board, valid_neighbors, x_or, FLOWDIR
from cnf import form_color_cnf, get_dir_var, form_dir_cnf
filename = 'puzzles/regular_6x6_01.txt'


def flow_free_main():
    """flow_free_main.

    DESCRIPTION: main function of the solver.
    INPUT: None
    OUTPUT: None
    """
    with open(filename, 'r', encoding='UTF-8') as input:
        board, colors = read_board(input)

    num_colors = len(colors)
    # get dimensions of the board
    width = len(board[0])
    height = len(board)

    num_cells = width * height
    num_cvars = num_cells * num_colors
    d_sat_var, var_count = get_dir_var(board, num_cvars)
    clauses = form_dir_cnf(board, colors, d_sat_var)
    print(clauses)



if __name__ == '__main__':

    flow_free_main()
