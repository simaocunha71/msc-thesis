```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure the strings are of equal length
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")

    # Convert the strings to lists of integers
    a = list(map(int, a))
    b = list(map(int, b))

    # Perform XOR operation on each pair of corresponding bits
    result = [str(x ^ y) for x, y in zip(a, b)]

    # Join the list of results into a single string and return
    return "".join(result)
```
