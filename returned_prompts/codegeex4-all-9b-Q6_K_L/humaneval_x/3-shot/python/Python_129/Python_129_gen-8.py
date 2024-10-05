    # Initialize a 2D array to store the minimum path value for each cell
    min_path = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]

    # Initialize the starting point
    start_row, start_col = 0, 0
    min_path[start_row][start_col] = grid[start_row][start_col]

    # Perform a breadth-first search to find the minimum path value for each cell
    queue = [(start_row, start_col)]
    while queue:
        row, col = queue.pop(0)

        # Check if we can move up
        if row > 0 and min_path[row-1][col] > min_path[row][col] + grid[row-1][col]:
            min_path[row-1][col] = min_path[row][col] + grid[row-1][col]
            queue.append((row-1, col))

        # Check if we can move down
        if row < len(grid) - 1 and min_path[row+1][col] > min_path[row][col] + grid[row+1][col]:
            min_path[row+1][col] = min_path[row][col] + grid[row+1][col]
            queue.append((row+1, col))

        # Check if we can move left
        if col > 0 and min_path[row][col-1] > min_path[row][col] + grid[row][col-1]:
            min_path[row][col-1] = min_path[row][col] + grid[row][col-1]
            queue.append((row, col-1))

        # Check if we can move right
        if col < len(grid[0]) - 1 and min_path[row][col+1] > min_path[row][col] + grid[row][col+1]:
            min_path[row][col+1] = min_path[row][col] + grid[row][col+1]
            queue.append((row, col+1))

    # Find the cell with the minimum path value
    min_row, min_col = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if min_path[i][j] < min_path[min_row][min_col]:
                min_row, min_col = i, j

    # Trace back the path from the minimum path value cell
    path = [grid[min_row][