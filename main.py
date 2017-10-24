"""main function running the whole puzzle solver."""

from utility import read_board, valid_neighbors

filename = 'puzzles/input55.txt'


def flow_free_main():
    """flow_free_main.

    DESCRIPTION: main function of the solver.
    INPUT: None
    OUTPUT: None
    """
    with open(filename, 'r', encoding='UTF-8') as input:
        board, colors = read_board(input)

    print(len(board))
    print(len(colors))
    print(valid_neighbors(4, 4, 5, 5))


if __name__ == '__main__':

    flow_free_main()
