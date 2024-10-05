    def max_fill(grid, capacity):
        total_water = sum([row.count(1) for row in grid])
        return math.ceil(total_water / capacity) if total_water > 0 else 0
    return max_fill(grid, capacity)  # Example usage


