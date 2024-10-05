    # Initialize a dictionary to store the minimum path for each cell
    dp = {}

    # Define the possible moves from a cell
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Define a helper function to find the minimum path
    def find_path(i, j, k):
        # If we have already computed the minimum path for this cell, return it
        if (i, j, k) in dp:
            return dp[(i, j, k)]

        # If we have reached the end of the path, return the current path
        if k == 0:
            return [grid[i][j]]

        # Initialize the minimum path
        min_path = None

        # Try all possible moves
        for di, dj in moves:
            ni, nj = i + di, j + dj

            # Check if the move is valid
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                # Recursively find the minimum path for the new cell
                path = find_path(ni, nj, k - 1)

                # If the path is shorter than the current minimum path, update it
                if min_path is None or path < min_path:
                    min_path = path + [grid[i][j]]

        # Store the minimum path
        dp[(i, j, k)] = min_path

        # Return the minimum path
        return min_path

    # Find the minimum path starting from each cell
    min_paths = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            min_paths.append(find_path(i, j, k))

    # Find the minimum path that is lexicographically smallest
    min_path = min(min_paths)

    # Return the minimum path
    return min_path
    pass


