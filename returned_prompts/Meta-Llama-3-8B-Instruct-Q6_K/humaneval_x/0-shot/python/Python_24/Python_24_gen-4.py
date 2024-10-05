The function `largest_divisor` finds the largest number that divides the input number `n` evenly, smaller than `n`.

Here's how you can implement it in Python:

```Python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor found, return 1
```

The function works by iterating from `n-1` down to `1` and checking if each number is a divisor of `n`. If a divisor is found, the function returns that divisor. If no divisor is found, the function returns `1`, which is a trivial divisor for any number. The `range` function is used with a step of `-1` to iterate in reverse order, and the `if` statement checks if the remainder of the division of `n` by `i` is `0`, which is the condition for `i` to be a divisor of `n`. 

For example, if you call `largest_divisor(15)`, the function will return `5`, because `5` is the largest number that divides `15` evenly, smaller than `15`.  If you call `largest_divisor(12)`, the function will return `6`, because `6` is the largest number that divides `12` evenly, smaller than `12`. If you call `largest_divisor(10)`, the function will return `5`, because `5` is the largest number that divides `10` evenly, smaller than `10`. If you call `largest_divisor(7)`, the function will return `1`, because `1` is the largest number that divides `7` evenly, smaller than `7`. 

This function works for any positive integer input.  If you want to handle negative integers or non-integer inputs, you would need to add additional error checking and handling code.  For example, you could check if the input is negative and return a message indicating that the function only works with positive integers.  You could also check if the input is not an integer and return a message indicating that the function only works with integers.  You could use a try-except block to catch