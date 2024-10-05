```python
def maxFill(grid, capacity):
    result = 0
    for row in grid:
        for i in range(0, len(row), capacity):
            result += (sum(row[i:i+capacity]) + capacity - 1) // capacity
    return result
```
