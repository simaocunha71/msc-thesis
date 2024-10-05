

def change_base(x: int, base: int) -> str:
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
        return change_base(x // base, base) + str(x % base)

print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))

# Output:
# 22
# 1000
# 111


This code is a recursive function that works by continually dividing the input number by the base and prepending the remainder to the result until the number is less than the base. The result is then converted to a string and returned.
</pre>
</details>

<details>
<summary>