Here is a Python solution for the problem:

```python
def maxFill(grid, capacity):
    count = 0
    for row in grid:
        level = 0
        for i, val in enumerate(row):
            if val == 1:
                level += 1
            if level == capacity:
                count += 1
                level = 0
        if level > 0:
            count += (level // capacity) + (1 if level % capacity != 0 else 0)
    return count

# Test cases
print(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # 6
print(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # 5
print(maxFill([[0,0,0], [0,0,0]], 5)) # 0
```

This solution works by iterating over each row in the grid, and for each row it keeps track of the number of wells that have been filled (i.e., the level). If the level reaches the bucket's capacity, it increments the count and resets the level. If the level is greater than 0 after iterating over the row, it calculates the number of buckets needed to empty the remaining water and increments the count accordingly. The function finally returns the total count of buckets needed.