Here's a Python function that checks whether the count of divisors of a number is even or not.

```python
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            count += 1
    if(count % 2 == 0):
        return True
    else:
        return False
```

Explanation:
The function `count_divisors` takes an integer `n` as input and initializes a variable `count` to 0. It then iterates through all numbers from 1 to `n` and checks if `n` is divisible by each of them. If it is, it increments the `count` variable by 1. After the loop, it checks if the `count` is even (i.e., divisible by 2) using the modulo operator (`%`). If it is, the function returns `True`, indicating that the count of divisors is even. Otherwise, it returns `False`.

You can use the `assert` statement to verify the correctness of the function. For example, `assert count_divisors(10)` will pass if the function correctly returns `True` for the input `10`.

```python
assert count_divisors(10)  # This will pass if the function returns True for the input 10
```

Note that the function assumes that the input `n` is a positive integer. It does not handle negative numbers or non-integer inputs.

Additionally, it's worth noting that the function may not be the most efficient solution for counting divisors, especially for large numbers. There are more optimized algorithms available, but they may be more complex to implement.

In case you are interested, here's an alternative solution that uses the `math.sqrt` function to optimize the computation. It's important to note that this solution assumes the input is a positive integer:

```python
from math import sqrt

def count_divisors(n):
    count = 0
    if(n < 4):
        return count
    else:
        sqrt_n = int(sqrt(n))
        for