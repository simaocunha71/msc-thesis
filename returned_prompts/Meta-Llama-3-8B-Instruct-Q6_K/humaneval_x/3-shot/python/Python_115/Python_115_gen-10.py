    def max_fill(grid, capacity):
        # Initialize count of fill operations
        count = 0
        
        # Iterate over each row in the grid
        for row in grid:
            # Initialize current fill amount
            fill_amount = 0
            
            # Iterate over each element in the row
            for element in row:
                # If the element is 1, increment the fill amount
                if element == 1:
                    fill_amount += 1
                # If the fill amount exceeds the bucket capacity, 
                # increment the count and reset the fill amount
                if fill_amount > capacity:
                    count += math.ceil(fill_amount / capacity)
                    fill_amount = 0
            # If there are remaining elements to be filled, 
            # increment the count and reset the fill amount
            if fill_amount > 0:
                count += math.ceil(fill_amount / capacity)
        
        return count


