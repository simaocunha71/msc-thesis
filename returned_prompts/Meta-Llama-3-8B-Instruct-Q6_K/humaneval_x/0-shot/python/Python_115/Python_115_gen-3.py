Here is a Python solution for the problem:

```
def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    res = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                res += math.ceil(grid[row][col] / capacity)
    return res
```

This solution iterates over each cell in the grid. If the cell contains water (i.e., the value is 1), it calculates the number of times the bucket needs to be lowered to extract the water using the formula `math.ceil(water_amount / capacity)`, where `water_amount` is the amount of water in the cell. The results are summed up to give the total number of times the buckets need to be lowered.

This solution has a time complexity of O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because it iterates over each cell in the grid once. The space complexity is O(1), which means it uses a constant amount of space, as it only uses a few variables to store the results. 