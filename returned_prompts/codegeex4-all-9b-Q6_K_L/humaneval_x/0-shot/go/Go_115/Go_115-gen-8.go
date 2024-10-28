def max_fill(grid, capacity):
    # Count the total number of water units in the grid
    total_water = sum(sum(row) for row in grid)

    # Initialize the number of buckets needed
    num_buckets = 0

    # Iterate through each row of the grid
    for row in grid:
        # Initialize the current row's water units
        current_row_water = 0

        # Iterate through each well in the row
        for well in row:
            # Add the current well's water units to the current row's water units
            current_row_water += well

            # If the current row's water units exceed the bucket's capacity,
            # increment the number of buckets needed and reset the current row's water units
            if current_row_water > capacity:
                num_buckets += 1
                current_row_water = 0

    # Return the number of buckets needed to empty the wells
    return num_buckets

