```python
def toggle_middle_bits(n):
    mask = (1 << n.bit_length() - 1) - 1
    return n ^ mask
```
