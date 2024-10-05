Here is a Python function that implements the problem:

```python
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

This function uses a for loop to iterate over the range from 1 to n (inclusive). For each number i, it checks if i is even by using the modulus operator (`i % 2 == 0`). If i is even, it calculates the factorial of i using a recursive function `factorial`. If i is odd, it calculates the sum of numbers from 1 to i using the built-in `sum` function and the `range` function. The calculated value is then appended to the result list. Finally, the function returns the result list.