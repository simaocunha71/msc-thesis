    rows, cols = len(grid), len(grid[0])
    max_fill_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_fill_count += math.ceil(grid[i][j] / capacity)

    return max_fill_count


