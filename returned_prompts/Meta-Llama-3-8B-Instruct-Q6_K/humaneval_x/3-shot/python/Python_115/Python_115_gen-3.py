    rows, cols = len(grid), len(grid[0])
    bucket_capacity = capacity
    buckets = math.ceil(sum(sum(row) for row in grid) / bucket_capacity)
    return buckets


