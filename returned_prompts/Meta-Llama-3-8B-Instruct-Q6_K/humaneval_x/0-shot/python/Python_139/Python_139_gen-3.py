```
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result
```
Explanation:
The function `special_factorial` calculates the special factorial of a given integer `n`. It does this by initializing a variable `result` to 1, then iterating over the range from 1 to `n` (inclusive). In each iteration, it multiplies the current value of `result` by the factorial of the current number `i`. Finally, it returns the calculated special factorial.

Note: The `math.factorial` function is used to calculate the factorial of a given number. This function is part of the Python `math` module. If you haven't imported the `math` module, you should do so by adding `import math` at the beginning of your code.