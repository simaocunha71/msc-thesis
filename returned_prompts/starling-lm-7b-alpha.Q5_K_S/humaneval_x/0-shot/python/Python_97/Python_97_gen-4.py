    # Your code here
    unit_digit_product = (a % 10) * (b % 10)
    return unit_digit_product







```
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    # Your code here
    unit_digit_product = (a % 10) * (b % 10)
    return unit_digit_product

```
Here's a breakdown of the solution provided:

1. The `multiply` function takes two integer arguments, `a` and `b`.
2. It uses the modulo operator `%` to get the unit digit of each number. The modulo operator returns the remainder when dividing `a` by 10 and `b` by 10, respectively.
3. The unit digit of a number is the rightmost digit. For example, the unit digit of 148 is 8, and the unit digit of 412 is 2.
4. The function then multiplies the unit digits of `a` and `b` together, storing the result in the variable `unit_digit_product`.
5. Finally, the function returns the value of `unit_digit_product`, which is the product of the unit digits of `a` and `b`.

By following these steps, the `multiply` function correctly calculates and returns the product of the unit digits of the given integers.

Examples of the function in use:
```python
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))    # Output: 72
print(multiply(2020