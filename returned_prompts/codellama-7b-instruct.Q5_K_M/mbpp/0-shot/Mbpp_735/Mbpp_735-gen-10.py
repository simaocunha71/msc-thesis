```
def toggle_middle_bits(n):
    if n == 0:
        return 0
    first_bit = n & 1
    last_bit = n & 1 << (n.bit_length() - 1)
    return (n ^ (n & (n - 1))) | first_bit | last_bit
```
