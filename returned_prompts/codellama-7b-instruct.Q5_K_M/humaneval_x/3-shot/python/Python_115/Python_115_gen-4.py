    def find_max(row):
        return max(row)

    def find_min(row):
        return min(row)

    def find_row_index(row):
        return row.index(min(row))

    def fill_well(row, i, j):
        if grid[i][j] == 1:
            grid[i][j] = 0
            return 1
        else:
            return 0

    def fill_row(row, j):
        count = 0
        for i in range(len(grid)):
            count += fill_well(row, i, j)
        return count

    def fill_grid(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if find_max(grid[i]) == 1:
                    fill_row(grid[i], j)

    def find_bucket_count(grid, capacity):
        count = 0
        for row in grid:
            for well in row:
                if well == 1:
                    count += 1
        return count // capacity

    grid_length = len(grid)
    if grid_length == 0:
        return 0

    if find_max(grid[0]) == 0:
        return 0

    fill_grid(grid)

    return find_bucket_count(grid, capacity)


