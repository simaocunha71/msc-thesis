    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                total += math.ceil(grid[i][j] / capacity)
    return total

