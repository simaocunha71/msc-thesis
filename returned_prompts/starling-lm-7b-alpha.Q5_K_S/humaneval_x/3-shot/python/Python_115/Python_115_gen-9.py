    def max_fill(grid, capacity):
        """
        Initialize max_fill as 0.

        While there are still 1s in the grid:
            Find the smallest row with at least one 1.
            Find the smallest column in that row with at least one 1.
            Empty all the 1s in that column up to the first 1 in that column in a new_row.
            Add the number of 1s in new_row to max_fill.
            Add the number of 1s in new_row to the number of 1s in the row with 1s.
            Truncate new_row to the capacity of the bucket.
            Add the new_row to the grid.
        Return max_fill.
        """
        def find_smallest_column(row):
            """
            Initialize smallest_column as the index of the first 1 in row.

            While there are still 1s in row:
                Find the smallest index i of 1 in row after smallest_column.
                If i is greater than smallest_column, add i to smallest_column.

            Return smallest_column.
            """
            smallest_column = grid[row].index(1)
            while grid[row].count(1) > smallest_column:
                smallest_column = grid[row].index(1, smallest_column)
            return smallest_column

        def find_smallest_row(grid):
            """
            Initialize smallest_row as the index of the first 1 in grid.

            While there are still 1s in grid:
                Find the smallest index i of 1 in grid after smallest_row.
                If i is greater than smallest_row, add i to smallest_row.

            Return smallest_row.
            """
            smallest_row = grid.index(1)
            while grid.count(1) > smallest_row:
                smallest_row = grid.index(1, smallest_row)
            return smallest_row

        def truncate_row(row, capacity):
            """
            Initialize new_row as row.

            While new_row has capacity or more 1s:
                Find the smallest