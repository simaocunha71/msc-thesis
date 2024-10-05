

def change_base(x, base):
    if not 2 <= base <= 10:
        raise ValueError("base should be between 2 and 10")

    if x < 0:
        return '-' + change_base(-x, base)

    if x < base:
        return str(x)

    return change_base(x // base, base) + str(x % base)


# Testing
# print(change_base(8, 3))  # '22'
# print(change_base(8, 2))  # '1000'
# print(change_base(7, 2))  # '111'

```

This implementation of `change_base` function is a recursive function that converts a numerical number `x` to a new base. It first checks if the `base` is within the acceptable range of 2 to 10 and raises a `ValueError` if it's not. Then it checks if the `x` is negative. If it's negative, it prefixes a `-` sign to the result of the function when `x` is converted to the `base`. If `x` is less than the `base`, it simply converts the `x` to a string. If `x` is greater than or equal to the `base`, it recursively calls the `change_base` function with `x` divided by the `base` and the `base` itself. Finally, it concatenates the result of the recursive call with the remainder of the division by the `base` and returns the result. 

The test cases provided at the end of the code demonstrate the functionality of the `change_base` function by converting a few numbers to different bases.

```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
