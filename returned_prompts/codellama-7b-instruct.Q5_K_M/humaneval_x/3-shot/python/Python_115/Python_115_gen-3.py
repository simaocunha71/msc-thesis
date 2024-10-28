    def get_well_index(row, column):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and i == row and j == column:
                    return i
        return -1

    def get_next_row(row, column, capacity):
        next_row = row
        while row < len(grid):
            if grid[row][column] == 1:
                break
            row += 1
        return row

    def get_next_column(row, column, capacity):
        next_column = column
        while column < len(grid[0]):
            if grid[row][column] == 1:
                break
            column += 1
        return column

    def get_water_count(row, column, capacity):
        water_count = 0
        while row < len(grid):
            while column < len(grid[0]):
                if grid[row][column] == 1:
                    water_count += 1
                    if water_count > capacity:
                        return capacity
                column += 1
            column = 0
            row += 1
        return water_count

    def get_row_count(row, column, capacity):
        row_count = 0
        while row < len(grid):
            if grid[row][column] == 1:
                row_count += 1
            row += 1
        return row_count

    def get_column_count(row, column, capacity):
        column_count = 0
        while column < len(grid[0]):
            if grid[row][column] == 1:
                column_count += 1
            column += 1
        return column_count

    def get_max_count(row, column, capacity):
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return 0
        if row == len(grid) - 1:
            return get_column_count(row, column, capacity)
        if column == len(grid[0