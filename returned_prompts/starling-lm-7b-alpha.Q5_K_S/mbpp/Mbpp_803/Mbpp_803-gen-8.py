To determine if a number is a perfect square, we can calculate its square root and check if it is an integer. Here's a step-by-step guide to accomplish this:

1. Define a function `is_perfect_square` that accepts a number `n` as an argument.
2. Inside the function, calculate the square root of `n` using the exponentiation operator (`**`). The square root is calculated as `n ** 0.5`.
3. Convert the square root to an integer using the `int()` function to remove any decimal places.
4. Check if the integer square root is equal to the original square root. If they are equal, the number is a perfect square and the function should return `True`. Otherwise, it's not a perfect square and the function should return `False`.
5. Test the function by asserting that `not is_perfect_square(10)` is `True`, indicating that 10 is not a perfect square.

Here's an example implementation of the `is_perfect_square` function:

```python
import math

def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
```

You can use this function to check if a number is a perfect square. For example, `is_perfect_square(16)` would return `True` because 16 is a perfect square, while `is_perfect_square(10)` would return `False` because 10 is not a perfect square.

To verify the function, we can use the `assert` statement to check that `not is_perfect_square(10)` is indeed `True`. This assertion ensures that the function correctly identifies 10 as not being a perfect square.

```python
assert not is_perfect_square(10)
```

This assertion will pass if the `is_perfect_square` function correctly identifies 10 as not being a perfect square.

Overall, this approach allows you to determine if a number is a perfect square by calculating its square root and checking if it is an integer.

"""

import math

