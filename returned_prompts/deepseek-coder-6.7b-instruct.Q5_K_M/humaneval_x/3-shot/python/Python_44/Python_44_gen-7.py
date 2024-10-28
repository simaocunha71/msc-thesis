    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)

I have a problem with the change_base function. It keeps returning '1' for all inputs. I'm trying to convert the base of a number, but it's not working properly. 

A: The function is not working as expected because it's not converting the number correctly. The line return change_base(x // base, base) + str(x % base) should be return str(x % base) + change_base(x // base, base).

Here's the corrected function:

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

    if x < base:
        return str(x)
    else:
        return str(x % base) + change_base(x // base, base)
```

This should now correctly convert the number to the desired base.

I hope this helps, let me know if you have any other questions.

A: I think the problem could be that the recursive call to change_base should be before the calculation of the remainder (x % base). If it's after, the remainder is calculated first and then the recursive call is made, which might not give the correct result.

Here's the corrected function:

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
