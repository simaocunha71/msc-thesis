    def get_values(grid):
        values = []
        for row in grid:
            for val in row:
                values.append(val)
        return values

    def get_neighbors(grid, row, col):
        neighbors = []
        if row - 1 >= 0:
            neighbors.append(grid[row - 1][col])
        if col - 1 >= 0:
            neighbors.append(grid[row][col - 1])
        if row + 1 < len(grid):
            neighbors.append(grid[row + 1][col])
        if col + 1 < len(grid[0]):
            neighbors.append(grid[row][col + 1])
        return neighbors

    def get_min_path_values(grid, k):
        values = get_values(grid)
        if k == 1:
            return values
        if k == len(values):
            return [1]
        if k > len(values):
            return None

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                neighbors = get_neighbors(grid, row, col)
                for neighbor in neighbors:
                    if neighbor in values:
                        values.remove(neighbor)
                        k -= 1
                        if k == 1:
                            return [neighbor] + get_min_path_values(grid, k)

        return None

    return get_min_path_values(grid, k)


