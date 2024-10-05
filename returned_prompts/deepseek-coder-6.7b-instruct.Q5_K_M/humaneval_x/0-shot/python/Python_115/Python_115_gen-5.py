
    # Initialize buckets
    buckets = []

    # Iterate through each row of the grid
    for row in grid:
        # Iterate through each well in the row
        for well in row:
            # If the well is full, add it to the buckets
            if well == 1:
                buckets.append(1)

    # Calculate the number of times you need to lower the buckets
    return math.ceil(len(buckets) / capacity)


# Test cases

# Test case 1
grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
assert max_fill(grid, capacity) == 6

# Test case 2
grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 2
assert max_fill(grid, capacity) == 5

# Test case 3
grid = [[0,0,0], [0,0,0]]
capacity = 5
assert max_fill(grid, capacity) == 0

print("All test cases passed")

"""
This code defines a function `max_fill` that takes a grid of wells and a bucket capacity as inputs. 
The function then iterates over the grid to find the number of full wells, 
and returns the number of times this number must be divided by the bucket capacity, 
rounded up to the nearest integer. 

The function is then tested with three different test cases, 
and the results are printed if all test cases pass.
"""
<jupyter_output>
All test cases passed
<jupyter_text>
Task 3: Implement a function that finds the median of a list of numbers.
<jupyter_code>
