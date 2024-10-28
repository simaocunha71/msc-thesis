
To determine if a number is prime, we can follow these steps:

1. Check if the given number is less than or equal to 1. If it is, return False because prime numbers are greater than 1.
2. Check if the number is divisible by 2. If it is, return False because even numbers (excluding 2) are not prime.
3. Iterate from 3 to the square root of the number (inclusive). For each iteration, check if the number is divisible by the current iteration. If it is, return False because the number is not prime. If the iteration completes without finding any divisors, return True because the number is prime.

Here's the Python code that implements these steps:

```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
```

You can test the function using the provided test cases:

```python
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

The function `is_prime` takes an integer `n` as input and returns True if `n` is prime, and False otherwise. It first checks if `n` is less than or equal to 1, in which case it immediately returns False. Then, it checks if `n` is divisible by 2, in which case it also returns False. Finally, it iterates from 3 to the square root of `n` (inclusive) and checks if `n` is divisible by any of these numbers. If it is, it returns False. If the iteration completes without finding any divisors, it returns True, indicating that `n` is prime.

The `