
Here's another way to solve this problem, using list comprehension and the `reduce` function from the `functools` module:

```python
from functools import reduce

def digits(n):
    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 != 0]
    return reduce(lambda x, y: x * y, odd_digits) if odd_digits else 0
```

This function also takes a positive integer `n` as input. It first creates a list `odd_digits` using list comprehension. It iterates over each character in the string representation of `