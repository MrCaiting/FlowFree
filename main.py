"""main function running the whole puzzle solver."""

from utility import *

filename = 'puzzles/input55.txt'


def flow_free_main():

    with open(filename, 'r', encoding='UTF-8') as input:
        board, colors = read_board(input)

    print(len(board))
    print(colors)
    print(valid_neighbors(4,4,5,5))

if __name__ == '__main__':

    flow_free_main()
