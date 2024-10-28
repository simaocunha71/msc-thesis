```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert strings to lists of integers
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    # Perform XOR operation on the lists
    result = [a[i] ^ b[i] for i in range(len(a))]

    # Convert the result list to a string
    return ''.join(str(x) for x in result)
```
