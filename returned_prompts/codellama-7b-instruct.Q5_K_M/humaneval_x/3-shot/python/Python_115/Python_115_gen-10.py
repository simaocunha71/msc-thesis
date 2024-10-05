    def max_fill(grid, capacity):
        import math
        grid_length = len(grid)
        grid_width = len(grid[0])
        total_water = 0
        total_buckets = 0
        for i in range(grid_length):
            for j in range(grid_width):
                if grid[i][j] == 1:
                    total_water += 1
        total_buckets = min(capacity, total_water)
        min_fill_per_bucket = math.ceil(total_water / total_buckets)
        return min_fill_per_bucket * total_buckets
