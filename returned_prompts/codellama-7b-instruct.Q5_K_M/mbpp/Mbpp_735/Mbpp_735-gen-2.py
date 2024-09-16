```
def toggle_middle_bits(n):
    n ^= n >> 1
    n ^= n >> 2
    n ^= n >> 4
    return n ^ 1
```
