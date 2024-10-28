Here is a Python solution for the problem:

```Python
def max_fill(grid, capacity):
    count = 0
    for row in grid:
        count += math.ceil(sum(row) / capacity)
    return count
```

This function iterates over each row in the grid, calculates the total amount of water in the row, and then divides it by the capacity of the bucket. It uses the `math.ceil` function to round up to the nearest whole number, because you can't extract a fraction of a bucket. Finally, it adds the result to the total count of times the bucket needs to be lowered.

For example, if the grid is `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and the capacity is 1, the function will calculate:

- `math.ceil(sum([0,0,1,0]) / 1) = math.ceil(1 / 1) = 1`
- `math.ceil(sum([0,1,0,0]) / 1) = math.ceil(1 / 1) = 1`
- `math.ceil(sum([1,1,1,1]) / 1) = math.ceil(4 / 1) = 4`

So the total count is 1 + 1 + 4 = 6. This is the correct answer for the given example.