To determine if a number is prime, you can follow these steps:

1. Check if the number is less than 2. If it is, return False, as prime numbers are greater than or equal to 2.
2. Check if the number is equal to 2. If it is, return True, as 2 is a prime number.
3. Check if the number is divisible by 2. If it is, return False, as even numbers (except 2) are not prime.
4. Iterate from 3 to the square root of the given number (inclusive). For each iteration, check if the number is divisible by the current iteration. If it is, return False, as the number is not prime.
5. If none of the above conditions are met, return True, as the number is prime.

Here's an implementation of the `is_prime` function that follows these steps:

```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

You can test the function with different numbers to verify its correctness:

```python
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

The function correctly identifies whether a given number is prime or not.

The time complexity of this function is O(sqrt(n)). This is because we need to iterate only up to the square root of the given number, as any factor of `n` must be less than or equal to its square root.

The space complexity is O(1) as we are not using any extra space that grows with the input size.

Overall, this