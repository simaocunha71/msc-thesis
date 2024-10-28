```
def change_base(x: int, base: int):
    if x == 0:
        return '0'
    digits = '0123456789'
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    return result
```

This function converts an integer `x` to a base `base` less than 10. It uses the `divmod` function to divide `x` by `base` and get the remainder. The remainder is used as an index to the `digits` string to get the corresponding digit in the new base. The result is built by concatenating the digits in reverse order. If `x` is 0, the function returns '0'.