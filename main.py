"""main function running the whole puzzle solver."""

from utility import read_board
from sat import sat

FILENAME = 'puzzles/input55.txt'
HEURISTIC = 'random'

def flow_free_main():
    """flow_free_main.

    DESCRIPTION: main function of the solver.
    INPUT: None
    OUTPUT: None
    """
    with open(FILENAME, 'r', encoding='UTF-8') as input:
        board, colors = read_board(input)

    # reduce problem to sat
    d_sat_var, num_vars, clauses, reduce_time = sat(board, colors)

    # input clauses into solver
    solution = sat_solver(clauses, HEURISTIC)

if __name__ == '__main__':

    flow_free_main()
