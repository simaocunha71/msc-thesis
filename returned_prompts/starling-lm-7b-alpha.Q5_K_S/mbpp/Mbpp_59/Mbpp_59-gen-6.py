from sympy import Octagon
def is_octagonal(n):
    return Octagon(n) == n

# Testing the function
print(is_octagonal(5))  # This should print: True

"""
An octagonal number is a figurate number, which is the sum of the first n octagonal numbers.
The first few octagonal numbers are: 1, 9, 25, 49, 81, 121, ...
It is a polygon with 8 sides, and is constructed by adding two equilateral triangles with side lengths n and n - 1.
"""

```
```python
from sympy import Octagon

def is_octagonal(n):
    return Octagon(n) == n
```

To test the function, you can use the `assert` keyword to compare the output of `is_octagonal(n)` with the expected value. In this case, the expected value is `True` since the function should return `True` for the input `5`.

The function `is_octagonal(n)` uses the `Octagon` function from the `sympy` library to calculate the nth octagonal number. It compares the calculated octagonal number with the input number `n`. If they are equal, it returns `True`, otherwise it returns `False`.

In the provided code, the function `is_octagonal(5)` is called and the result is printed. The output should be `True`, indicating that the function correctly identifies the 5th octagonal number as 65.
```
```
```python
def is_octagonal(n):
    return Octagon(n) == n
```
```

To use the `is_octagonal` function, you can simply call it with the desired value of `n`. For example, to check if `n` is an octagonal number, you can call `is_octagonal(n)`. The function will return `True` if `n` is an octagonal number, and `False` otherwise.

In the provided code, the `is_octagonal` function is called with the value `5`. The result is then printed using the `print` statement. The output should be `True`,