    row = len(grid)
    col = len(grid[0])

    left = [0] * col
    right = [0] * col

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                continue

            if i == 0:
                left[j] = grid[i][j]
            else:
                left[j] = max(left[j], grid[i-1][j])

            if i == row-1:
                right[j] = grid[i][j]
            else:
                right[j] = max(right[j], grid[i+1][j])

    total = 0
    for i in range(col):
        total += min(left[i], right[i])

    return total // capacity
