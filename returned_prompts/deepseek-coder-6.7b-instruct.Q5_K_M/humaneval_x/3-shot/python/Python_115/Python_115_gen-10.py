    count = 0
    total_water = sum(sum(row) for row in grid)
    while total_water > 0:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_water -= capacity
                    count += 1
                    if total_water <= 0:
                        return count
                    grid[i][j] = 0
    return count


