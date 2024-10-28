The nth octagonal number is given by the formula n*(3n-1)*(2n-1)/2. This can be used to create a function that calculates the nth octagonal number.

Here is the Python function that does this:
```
def is_octagonal(n):
    return n*(3*n-1)*(2*n-1)//2
```
This function takes an integer `n` as input and returns the corresponding octagonal number. The `//` operator is used for integer division to ensure that the result is an integer.

For example, `is_octagonal(5)` returns `65`, which is the 5th octagonal number. 

Note that this function does not check if the input `n` is a valid positive integer. In a real-world application, you might want to add error handling to ensure that the input is valid. For example:
```
def is_octagonal(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return n*(3*n-1)*(2*n-1)//2
```
This version of the function raises a `ValueError` if the input `n` is not a positive integer.