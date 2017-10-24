"""cell_colo.py file."""
from utility import FLOWDIR
from utility import or_seq
from utility import valid_neighbors
from utility import x_or


def get_cell_cIndex(row_size, i, j, all_colors, curr_color):
    """get_cell_cIndex.

    DESCRIPTION: helper function used to return the calculated index of the
        the current cell based on its location and the color it has.
    INPUTS:
        1. row_size: how many columns exist in the board
        2. i,j: the coordinate that indicates where's the cell at
        3. all_colors: a list of all colors that are available
        4. curr_color: the current color of the cell
    OUTPUT:
        The calculated index
    """
    num_colors = len(all_colors)
    index = (i*row_size + j)*num_colors + curr_color + 1   # add 1 in case of 0
    return index


def dir_sat_var(maze, curr_cell):
    """dir_sat_var.

    DESCRIPTION: get input current direction bit and check what future flow direction is
        allowed.
        The direction in FLOWDIR will contains all possible flow structure direction, but
        not all of them will be available based on the information that we previously got
        about which neighbors are available
    INPUTS:
        curr_dir: Binary bit string that contains the all possible neighbors direction
        which is formed by previously applying bitwise OR on a sequence
    """
    maze_height = len(maze)     # Since the maze passed in is a list of rows
    maze_width = len(maze[0])   # Get the number of columns
    d_sat_var = dict()
    var_count = 0

    for i, rows in enumerate(maze):
        for j, cell in enumerate(maze):
            # Jump over all the enp
            if cell.isalpha():
                continue

            neighbors = valid_neighbors(i, j, maze_width, maze_height)
            # Make a list to hold all the direction bits from neighbors
            all_nei_dir = []
            for direction, _, _, in neighbors:
                all_nei_dir.append(direction)

            dir_result = or_seq(all_nei_dir)
            d_sat_var[i, j] = dict()

            for flow_dir in FLOWDIR:
                if dir_result & flow_dir == flow_dir:
                    # If this possible direction is possible, increase the count
                    var_count = var_count + 1
                    dir_sat_var[i, j][flow_dir] = curr_cell + var_count

    return dir_sat_var, var_count


def form_color_cnf(maze, all_colors):
    """from_color_cnf.

    DESCRIPTION: use this method to generate a proper CNF based on the color
        assignment that we have. The constraints that we will apply here are:
        1. Every cell is assigned a color and ONLY one color
        2. No two color assignment will ever be true on a single cell
        3. No two any more neighbors of the end points will share same color
    INPUTs:
        1. maze: the array format of the parsed maze
        2. all_colors: a dictionary of all colors that are available on the
            board as the keys, and their values are the order of how they
            are been discovered
    """
    cnf = []    # a list holding all formed CNF
    maze_height = len(maze)     # Since the maze passed in is a list of rows
    maze_width = len(maze[0])   # Get the number of columns

    for i, rows in enumerate(maze):
        for j, cell in enumerate(maze):
            if cell.isalpha():      # Check if this cell is an endpoint
                cell_color = all_colors[cell]
                cnf.append(get_cell_cIndex(maze_width, i, j, all_colors, cell_color))

                # Since we have a color assigned, no more should be allowed
                for key, value in all_colors.items():
                    if value != cell_color:

                        # append negative value if the color is not right
                        cnf.append(-get_cell_cIndex(maze_width, i, j, all_colors, value))

                # Checking if the cell has neighbors with similar colors
                neighbors = valid_neighbors(i, j, maze_width, maze_height)
                nei_color = []
                for _, di, dj in neighbors:
                    nei_color.append(get_cell_cIndex(maze_width, di, dj, all_colors, cell_color))

                cnf.append(nei_color)

                cnf.extend(x_or(nei_color))

            else:       # The place corresponds to an empty space
                possible_colors = []
                for key, value in all_colors.items():
                    temp_index = get_cell_cIndex(maze_width, i, j, all_colors, value)
                    cnf.append(temp_index)
                    possible_colors.append(temp_index)

                cnf.extend(x_or(possible_colors))

    return cnf
