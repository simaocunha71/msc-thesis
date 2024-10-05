    def fill_grid(grid, capacity):
        """Helper function to fill the grid with water"""
        grid_filled = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < capacity:
                    grid_filled[i][j] = grid[i][j]
                else:
                    grid_filled[i][j] = capacity

        return grid_filled

    def count_buckets(grid, grid_filled):
        """Helper function to count the number of buckets needed to empty the grid"""
        bucket_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != grid_filled[i][j]:
                    bucket_count += 1
        return bucket_count

    grid_filled = fill_grid(grid, capacity)
    bucket_count = count_buckets(grid, grid_filled)

    return math.ceil(bucket_count/capacity)


