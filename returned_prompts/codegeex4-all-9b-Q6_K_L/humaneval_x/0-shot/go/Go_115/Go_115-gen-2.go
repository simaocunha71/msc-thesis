def max_fill(grid, capacity):
    # Initialize the number of times you need to lower the buckets
    times = 0
    
    # Iterate through each row in the grid
    for row in grid:
        # Initialize the number of units of water in the current well
        water = 0
        
        # Iterate through each unit in the row
        for unit in row:
            # If the unit contains water
            if unit == 1:
                # Add one unit of water to the current well
                water += 1
        
        # Calculate the number of times you need to lower the buckets for the current well
        times += math.ceil(water / capacity)
    
    # Return the total number of times you need to lower the buckets
    return times

