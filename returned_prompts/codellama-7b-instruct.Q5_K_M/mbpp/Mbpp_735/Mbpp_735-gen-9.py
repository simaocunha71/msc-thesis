```
def toggle_middle_bits(n):
    mask = ~0x3
    return (n | 0x1) & mask
```
