Here is a Python solution for the problem. This solution uses a greedy approach to solve the problem.

```
def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    max_water = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_water += 1
    return math.ceil(max_water / capacity)
```

The function `max_fill` takes a 2D list `grid` and an integer `capacity` as input. It returns the minimum number of times the bucket needs to be lowered to empty the wells.

The function first calculates the total amount of water in the wells by summing up all the 1's in the grid. Then, it calculates the minimum number of times the bucket needs to be lowered by dividing the total amount of water by the capacity of the bucket and rounding up to the nearest integer.

The time complexity of this function is O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because the function needs to iterate over each cell in the grid once. The space complexity is O(1), which means the function uses a constant amount of space. This is because the function only uses a fixed amount of space to store the variables and does not use any data structures that scale with the input size. 







