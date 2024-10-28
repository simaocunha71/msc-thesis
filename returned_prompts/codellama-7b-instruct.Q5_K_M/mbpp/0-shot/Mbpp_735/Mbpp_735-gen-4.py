```python
def toggle_middle_bits(n):
    first_bit, last_bit = n & 1, n & 2**(n.bit_length() - 1)
    return (n ^ 2**(n.bit_length() - 1)) | first_bit | last_bit
```
