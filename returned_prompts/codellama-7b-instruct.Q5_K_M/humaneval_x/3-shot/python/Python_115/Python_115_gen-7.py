    def get_max_value(grid):
        max_value = -1
        for row in grid:
            max_value = max(max_value, max(row))
        return max_value

    def get_max_row(grid):
        max_row = -1
        for i in range(len(grid)):
            if grid[i][0] > max_row:
                max_row = grid[i][0]
        return max_row

    def get_max_column(grid):
        max_column = -1
        for i in range(len(grid)):
            if grid[0][i] > max_column:
                max_column = grid[0][i]
        return max_column

    def get_total_rows(grid):
        return len(grid)

    def get_total_columns(grid):
        return len(grid[0])

    def get_total_units(grid):
        return sum(sum(row) for row in grid)

    def get_total_wells(grid):
        return len(grid) * len(grid[0])

    def get_well_index(grid, row, column):
        return row * len(grid[0]) + column

    def get_well_value(grid, row, column):
        return grid[row][column]

    def get_row_index(grid, well_index):
        return well_index // len(grid[0])

    def get_column_index(grid, well_index):
        return well_index % len(grid[0])

    def get_well_neighbours(grid, row, column):
        neighbours = []
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if i != row or j != column:
                        neighbours.append(get_well_index(grid, i, j))
        return neighbours

    def get_well_neighbour_values(grid,