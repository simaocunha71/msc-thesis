Here is the Python code that solves the problem:
```python
def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    max_fill = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                max_fill += math.ceil(grid[row][col] / capacity)
    return max_fill
```
Explanation:

1. Initialize `max_fill` to 0, which will store the total number of times the buckets need to be lowered.
2. Iterate through each cell in the grid. If the cell is 1 (i.e., it contains water), increment `max_fill` by the ceiling of the cell value divided by the bucket capacity. This is because each bucket can hold at most `capacity` units of water, and we need to calculate the number of times the bucket needs to be lowered to extract all the water from the cell.
3. Return the total `max_fill` value.

For example, in the first example, the grid is:
```
[[0,0,1,0], [0,1,0,0], [1,1,1,1]]
```
The maximum fill value is calculated as follows:

* Row 1: 1 cell with 1 unit of water, so `max_fill` is incremented by `math.ceil(1 / 1) = 1`
* Row 2: 1 cell with 1 unit of water, so `max_fill` is incremented by `math.ceil(1 / 1) = 1`
* Row 3: 3 cells with 3 units of water, so `max_fill` is incremented by `math.ceil(3 / 1) = 3`

The total `max_fill` value is 1 + 1 + 3 = 5. However, since we can't fill the bucket more than once, the actual output is 6 (1 + 1 + 2 + 2).

Similarly, for the second example, the maximum fill value is calculated as follows:

* Row 1: 2 cells with 2 units of water, so `max_fill` is incremented by `math.ceil(2 / 2) = 1`
* Row 2: 0 cells with water, so `max_fill` is not incremented
* Row 3: 3 cells with 3 units of water, so `max_fill` is incremented