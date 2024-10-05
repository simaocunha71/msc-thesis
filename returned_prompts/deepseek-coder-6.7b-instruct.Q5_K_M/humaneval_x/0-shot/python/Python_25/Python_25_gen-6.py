Here is a Python program to solve the problem:

```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while(divisor <= n):
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors
```

In the above code, we start from the smallest possible factor, which is 2. We continue dividing the given number by the divisor until it is no longer divisible. If it is not divisible, then we increase the divisor by 1. This process continues until the divisor is greater than the given number.

This program returns the list of prime factors of the given number, each of which is listed the number of times corresponding to how many times it appears in the factorization.

Let's test the function with your examples:

```python
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

As you see, this program works correctly, and it returns the correct list of prime factors for the given numbers.

Note: This program assumes that the input number is a positive integer. If the input number is zero or negative, the program should return an appropriate error message.
