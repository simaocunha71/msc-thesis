```python
def maxFill(grid, capacity):
    result = 0
    for row in grid:
        fill = 0
        for well in row:
            if well == 1:
                fill += 1
        result += (fill + capacity - 1) // capacity
    return result
```
