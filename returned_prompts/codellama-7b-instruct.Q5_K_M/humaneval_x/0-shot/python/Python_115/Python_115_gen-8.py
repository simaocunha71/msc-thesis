
def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    max_well_water = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_well_water += 1
    
    return min(max_well_water, capacity)
    
