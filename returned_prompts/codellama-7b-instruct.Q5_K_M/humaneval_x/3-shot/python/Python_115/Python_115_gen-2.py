    def get_row_water(row):
        water = 0
        for i in row:
            if i == 1:
                water += 1
        return water

    def get_column_water(column):
        water = 0
        for i in column:
            if i == 1:
                water += 1
        return water

    def get_row_bucket(row, capacity):
        if get_row_water(row) == 0:
            return 0

        water = 0
        for i in row:
            if i == 1:
                water += 1

        if water <= capacity:
            return 0

        return int(water / capacity)

    def get_column_bucket(column, capacity):
        if get_column_water(column) == 0:
            return 0

        water = 0
        for i in column:
            if i == 1:
                water += 1

        if water <= capacity:
            return 0

        return int(water / capacity)

    def get_row_index(grid, row_idx, capacity):
        if get_row_bucket(grid[row_idx], capacity) == 0:
            return 0

        if get_row_bucket(grid[row_idx], capacity) == 1:
            return 1

        return int(get_row_bucket(grid[row_idx], capacity) / 2) + 1

    def get_column_index(grid, column_idx, capacity):
        if get_column_bucket(grid[:, column_idx], capacity) == 0:
            return 0

        if get_column_bucket(grid[:, column_idx], capacity) == 1:
            return 1

        return int(get_column_bucket(grid[:, column_idx], capacity) / 2) + 1

    def get_row_index_in_range(grid, row_idx, capacity):
        row_water = get_row_water(grid[row_idx])
        row_bucket = get_row_bucket(grid[row_idx], capacity