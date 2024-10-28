```python
def set_left_most_unset_bit(n):
    i = 1
    while n & i:
        i <<= 1
    return n | i
```
