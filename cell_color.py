"""cell_colo.py file."""


def get_cell_index(maze, i, j, all_colors, curr_color):
    """
    get_cell_index.

    DESCRIPTION: helper function used to return the calculated index of the
        the current cell based on its location and the color it has.
    INPUTS:
        1. maze: the array format of the parsed maze
        2. i,j: the coordinate that indicates where's the cell at
        3. all_colors: a list of all colors that are avaible
        4. curr_color: the current color of the cell
    OUTPUT:
        The calculated index
    """
    row_size = len(maze)    # Since the maze always has square shape
    num_colors = len(all_colors)
    index = (i*row_size + j)*num_colors + curr_color + 1   # add 1 in case of 0
    return index


def form_color_cnf(maze, all_colors):
    """
    from_color_cnf.

    DESCRIPTION: use this method to generate a proper CNF based on the color
        assignment that we have. The constraints that we will apply here are:
        1. Every cell is assigned a color and ONLY one color
        2. No two color assignment will ever be true on a single cell
        3. No two any more neighbors of the end points will share same color
    INPUTs:
        1. maze: the array format of the parsed maze
        2. all_colors: a list of all colors that are avaible
    """
    cnf = []    # a list holding all formed CNF
    maze_length = len(maze)     # Since the maze passed in is a list of rows
    maze_width = len(maze[0])   # Get the number of columns

    for i, rows in enumerate(maze):
        for j, cell in enumerate(maze):
            if cell.isalpha():      # Check if this cell is an endpoint
                cell_color = all_colors[cell]
                cnf.append[get_cell_index(i, j, cell_color)]
                # Since we have a color assigned, no more should be allowed
