    def fill_buckets(grid, capacity):
        buckets = 0
        for row in grid:
            buckets += sum(row)
        return math.ceil(buckets / capacity)

    return fill_buckets(grid, capacity)


