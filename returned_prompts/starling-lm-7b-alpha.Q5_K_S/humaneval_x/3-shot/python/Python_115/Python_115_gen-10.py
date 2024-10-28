    def max_fill_helper(grid, row, capacity, count):
        if row == len(grid):
            return count

        if grid[row] == [0] * len(grid[row]):
            return max_fill_helper(grid, row + 1, capacity, count)

        if sum(grid[row]) % capacity == 0:
            return max_fill_helper(grid, row + 1, capacity, count + sum(grid[row]) // capacity)

        else:
            return max_fill_helper(grid, row + 1, capacity, count + (sum(grid[row]) // capacity + 1))

    return max_fill_helper(grid, 0, capacity, 0)


