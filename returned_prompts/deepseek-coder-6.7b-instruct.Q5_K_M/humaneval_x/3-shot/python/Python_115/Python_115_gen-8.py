    def max_fill(grid, capacity):
        total_wells = 0
        for row in grid:
            total_wells += sum(row)
        return math.ceil(total_wells / capacity)


