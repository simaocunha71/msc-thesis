    num_rows = len(grid)
    num_cols = len(grid[0])

    num_buckets = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                num_buckets += math.ceil(grid[row][col] / capacity)

    return num_buckets

