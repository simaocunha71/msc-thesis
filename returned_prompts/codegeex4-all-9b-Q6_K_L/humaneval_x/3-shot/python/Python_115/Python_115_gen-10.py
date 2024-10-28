    def fill(well):
        filled = 0
        for i in range(len(well)):
            if well[i] == 1:
                filled += 1
                well[i] = 0
        return filled

    def empty(well, capacity):
        empty = 0
        for i in range(len(well)):
            if well[i] == 0:
                well[i] = 1
                empty += 1
                if empty == capacity:
                    break
        return empty

    total_fill = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            well = grid[i][j]
            while fill(well) > 0:
                total_fill += empty(well, capacity)
    return total_fill

