Here is the Python function:

```python
def power_base_sum(base, power):
    return sum(int(digit) for digit in str(base ** power))

print(power_base_sum(2, 100))  # Output: 115
```

In this function, `base ** power` is used to calculate the power of the base, and `str(base ** power)` is used to convert the result into a string. Then, `int(digit) for digit in str(base ** power)` is used to convert each digit of the string back to an integer. Finally, `sum()` is used to calculate the sum of all the digits.

Note that this function uses `**` operator to calculate the power, which is a built-in Python operator. It also uses `sum()` function to calculate the sum of all digits, which is a built-in Python function.

This function works for positive integer base and power. For negative power, it will calculate the power of the reciprocal of the base. For zero power, it will return 1.
"""

