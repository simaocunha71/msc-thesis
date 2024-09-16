```python
def perfect_squares(low, high):
    return [x**2 for x in range(low, high+1) if x**2 <= high]
```
