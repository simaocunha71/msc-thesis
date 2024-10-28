    def count_well(row):
        return sum(row)

    def fill_row(row, capacity):
        filled = 0
        for i, cell in enumerate(row):
            if cell == 1:
                row[i] = 0
                filled += 1
                if filled == capacity:
                    break
        return filled

    def fill_column(grid, col, capacity):
        filled = 0
        for row in grid:
            filled += fill_row(row, capacity)
        return filled

    filled = 0
    for col in range(len(grid[0])):
        filled += fill_column(grid, col, capacity)

    return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1) for row in grid)
    # else:
    #     filled = 0
    #     for row in grid:
    #         filled += fill_row(row, capacity)
    #     return filled

    # if capacity == 1:
    #     return sum(row.count(1