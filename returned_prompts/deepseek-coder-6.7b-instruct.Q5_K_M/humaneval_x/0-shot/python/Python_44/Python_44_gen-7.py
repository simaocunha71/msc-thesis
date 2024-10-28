
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
    """
    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result
```

This function works by continuously dividing the input number by the target base, appending the remainder to the result string. This process is repeated until the number is zero. At the end, the result string is returned, which represents the input number in the target base.

It's important to note that the function assumes that the input number and the base are both valid integers. If the input number is less than zero or if the base is not between 2 and 10, the function may not behave as expected.

Also, the function does not handle cases where the base is 10 or greater. Converting to and from base 10 can be done using the built-in functions `bin()`, `oct()`, and `hex()` respectively, which are more efficient and easier to use.

Here's how you can use it:

```python
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

This will print the decimal number 8 converted to base 3, 2, and 2, respectively.

```python
print(bin(8))  # Outputs: '0b1000'
print(oct(8))  # Outputs: '0o1000'
print(hex(8))  # Outputs: '0x8'
```

These are the built-in functions that Python provides for converting between different bases. They are