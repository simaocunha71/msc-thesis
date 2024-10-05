
def max_fill(grid, capacity):
    import math
    # Initialize the number of times the bucket needs to be lowered.
    num_of_times_lowered = 0
    # Initialize the number of 1's in the grid.
    num_of_ones = 0
    # Loop through each row of the grid.
    for i in range(len(grid)):
        # Loop through each column of the grid.
        for j in range(len(grid[i])):
            # If the current element is a 1, we increment the number of 1's.
            if grid[i][j] == 1:
                num_of_ones += 1
    # If the number of 1's is greater than the capacity, then we need to lower the bucket.
    if num_of_ones > capacity:
        num_of_times_lowered += 1
        # If the number of 1's is greater than or equal to the capacity, then we need to lower the bucket.
        while num_of_ones >= capacity:
            # Loop through each row of the grid.
            for i in range(len(grid)):
                # Loop through each column of the grid.
                for j in range(len(grid[i])):
                    # If the current element is a 1, we decrement the number of 1's.
                    if grid[i][j] == 1:
                        num_of_ones -= 1
            # If the number of 1's is greater than or equal to the capacity, then we need to lower the bucket.
            if num_of_ones >= capacity:
                num_of_times_lowered += 1
    # Return the number of times the bucket needs to be lowered.
    return num_of_times_lowered

Test Cases:

grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
print(max_fill(grid, 1))

grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]