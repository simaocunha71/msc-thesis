```python
def toggle_middle_bits(n):
    """
    :param n: integer
    :return: integer
    """
    mask = 0x3333333333333333
    return (n ^ mask) + 1
```
