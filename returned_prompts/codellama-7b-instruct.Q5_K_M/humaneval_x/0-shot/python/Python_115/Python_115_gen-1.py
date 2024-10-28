    def max_fill(grid, capacity):
        # Find the number of rows and columns in the grid
        # Initialize the number of times we need to lower the bucket
        # Initialize the row and column index
        rows, cols = len(grid), len(grid[0])
        num_times = 0
        row, col = 0, 0

        # Loop through each row and column in the grid
        while row < rows and col < cols:
            # If we encounter a 1, add the capacity to the running total
            if grid[row][col] == 1:
                num_times += capacity
            # If we encounter a 0, move on to the next column
            else:
                col += 1
            # If we have reached the end of the row, move on to the next row
            if col == cols:
                row += 1
                col = 0

        # If there are still rows left to process, add the number of remaining rows
        # to the running total
        if row < rows:
            num_times += rows - row

        return num_times


