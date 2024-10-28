Here is the Python function to solve the problem:

```Python
def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    total_water = 0
    for row in grid:
        total_water += sum(row)
    return math.ceil(total_water / capacity)
```

This function works by first calculating the total amount of water in the grid by summing up all the 1s in the grid. Then, it returns the ceiling of the total water divided by the capacity of the bucket. The ceiling function is used to ensure that the bucket is filled at least once before being lowered. 

For example, if the total water is 12 and the bucket capacity is 3, the function will return 5 (since 12 / 3 is 4 and the ceiling of 4 is 5). This means that the bucket needs to be lowered 5 times to empty the wells. 

Note that the function assumes that the input grid is a list of lists, where each inner list represents a row in the grid. The function also assumes that the input capacity is a positive integer. If the input grid or capacity is invalid, the function may not work correctly. 

Also, note that this function does not actually fill the buckets or lower them, it just calculates how many times the buckets need to be lowered. If you want to implement the actual filling and lowering of the buckets, you would need a different function. 

This function is efficient because it only needs to iterate over the grid once to calculate the total amount of water, and then it can calculate the number of times the buckets need to be lowered in constant time. Therefore, the time complexity of this function is O(m*n), where m is the number of rows in the grid and n is the number of columns. The space complexity is O(1), since the function only uses a constant amount of space to store the total water and the result. 