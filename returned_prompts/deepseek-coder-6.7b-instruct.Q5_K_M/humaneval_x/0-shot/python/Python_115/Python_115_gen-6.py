
def max_fill(grid, capacity):
    water = sum(sum(row) for row in grid)
    return math.ceil(water / capacity)

# Test cases
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # Output: 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # Output: 5
print(max_fill([[0,0,0], [0,0,0]], 5)) # Output: 0

This solution works by summing up all the water in the grid and dividing it by the bucket capacity to get the number of times the buckets need to be lowered. The math.ceil function is used to round up to the nearest whole number, as you can't partially lower a bucket. This approach assumes that each row of the grid represents a well and that each 1 in the row represents a unit of water.

The time complexity of this solution is O(n*m) because it needs to iterate over each cell in the grid once, and the space complexity is O(1) because it uses a constant amount of space.

The constraints in the question specify that the grid will have dimensions up to 100x100, and the bucket capacity will be a number up to 10. This makes this solution efficient for these kinds of inputs.

Note: This solution assumes that the grid is a list of lists, where each inner list represents a row of the grid, and each element in the row is either 0 or 1.

The function max_fill takes in a grid and a bucket capacity, and returns the number of times the buckets need to be lowered to empty all the wells.
    """

# -------------------------SOLUTION END-----------------------------
<jupyter_output>
<empty_output>
<jupyter_text>
**Task 2**
<jupyter_code>
# -------------------------SOLUTION START-----------------------------
