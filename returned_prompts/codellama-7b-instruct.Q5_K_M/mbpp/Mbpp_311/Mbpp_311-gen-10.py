```
def set_left_most_unset_bit(n):
    mask = 0xAAAAAAAA
    mask &= n
    mask = ~mask
    return n | mask
```
