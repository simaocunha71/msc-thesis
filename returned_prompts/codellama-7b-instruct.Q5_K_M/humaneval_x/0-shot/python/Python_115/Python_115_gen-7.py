
    def max_fill(grid, capacity):
        # Calculate the number of rows and columns
        num_rows, num_cols = len(grid), len(grid[0])
        
        # Initialize the number of times we need to lower the buckets to 0
        num_buckets_lowered = 0
        
        # Loop through each row
        for i in range(num_rows):
            # Initialize the total number of units of water in the row to 0
            total_water = 0
            
            # Loop through each column
            for j in range(num_cols):
                # If the current cell is 1 (representing a unit of water)
                if grid[i][j] == 1:
                    # Increment the total number of units of water in the row
                    total_water += 1
                    
                    # If the total number of units of water in the row exceeds the capacity
                    if total_water > capacity:
                        # Increment the number of times we need to lower the buckets
                        num_buckets_lowered += 1
                        
                        # Reset the total number of units of water in the row to 0
                        total_water = 0
                        
        # Return the number of times we need to lower the buckets
        return num_buckets_lowered