"""main function running the whole puzzle solver."""

from utility import read_board
from read_cnf import convert
from sat import sat, decode, visualize
from solver import solve
from time import clock

FILENAME = 'puzzles/input991.txt'
# choose random_heuristic or POSIT
HEURISTIC = 'POSIT'
# Enable color print mode in terminal
COLOR_ENABLE = True


def flow_free_main():
    """flow_free_main.

    DESCRIPTION: main function of the solver.
    INPUT: None
    OUTPUT: None
    """
    print("To Change to Color Mode Visualization, Set COLOR_ENABLE to True.\n")
    print("Color Print Mode is Now %s\n" % ('Enabled' if COLOR_ENABLE is True else 'Disabled'))

    with open(FILENAME, 'r', encoding='UTF-8') as input:
        board, colors = read_board(input)

    # reduce problem to sat
    d_sat_var, num_vars, clauses, reduce_time = sat(board, colors)
    print("\nTime Used on Reducing the Problem to SAT: %.5f seconds\n" % reduce_time)
    # Get the CNF structured Formula
    CNF = convert(clauses, HEURISTIC)

    # input clauses into solver
    # clock time
    branch_count = [0, 0]
    print("Solving the Problem Using DPLL with [%s] Heuristic ...\n" % HEURISTIC)
    start = clock()
    # branch[0] is count of failure, branch[1] is count of success
    solved_cnf, branch = solve(CNF, branch_count)
    solve_time = clock() - start

    print("Time Used on Solving the SAT Problem: %.5f seconds\n" % solve_time)
    print("Failed Splits: ", branch[0])
    print("Successful Splites: ", branch[1])
    # Get the solution from the returing list
    solution = solved_cnf.get_solution()

    # Test line
    # print("SAT Solution: ", solution)
    # print("Type of sol: ", type(solution))

    # decode the solution
    converted = decode(board, colors, solution)

    # visialize the solution
    print("\nVisualized Solution: \n")
    visualize(converted, colors, COLOR_ENABLE)


if __name__ == '__main__':

    flow_free_main()
