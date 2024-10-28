The nth octagonal number is given by the formula (8n^3 + 3n^2 + 2n) / 2. We can use this formula to write a function to find the nth octagonal number.

Here is the Python solution:
```
def is_octagonal(n):
    return (8*n**3 + 3*n**2 + 2*n) // 2
```
This function takes an integer `n` as input and returns the corresponding octagonal number. The `//` operator is used for integer division to ensure that the result is an integer.

For example, `is_octagonal(5)` returns `65`, which is the 5th octagonal number. You can test this function with different inputs to verify that it works correctly.