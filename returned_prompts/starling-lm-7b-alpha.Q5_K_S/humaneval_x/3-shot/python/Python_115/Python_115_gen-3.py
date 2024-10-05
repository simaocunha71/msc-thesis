    def max_fill(grid, capacity):
        """
        Calculate the number of buckets needed to empty all wells.
        """
        rows = len(grid)
        cols = len(grid[0])
        total_units = 0

        for row in grid:
            total_units += sum(row)

        return math.ceil(total_units / capacity)


