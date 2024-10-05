Here's a Python solution to this problem:

```python
def maxFill(grid, capacity):
    count = 0
    for row in grid:
        while sum(row) > 0:
            count += 1
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                    if sum(row) <= capacity:
                        break
    return count
```

This function works by iterating over each row in the grid. For each row, it counts the number of times it needs to lower the bucket until all of the wells are empty.

It does this by iterating over each cell in the row, and if the cell contains water (1), it empties the bucket by setting the cell's value to 0. It then continues to the next cell until the row is empty or the bucket is full.

Finally, it returns the total number of times the bucket was lowered.