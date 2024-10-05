```python
def maxFill(grid, capacity):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cnt += (grid[i][j] + capacity - 1) // capacity
    return cnt
```
