
To solve this problem, we can start by finding the prime factors of the given number. We can use a function that checks if a number is prime and another function that finds all prime factors of a given number. Here's a step-by-step breakdown of the solution:

1. Create a function called `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise. This function will be used to check if a number is prime.

2. Create a function called `prime_factors` that takes a number as input and returns a list of its prime factors. This function will be used to find all prime factors of a given number.

3. Use the `is_prime` function to check if the input number is prime. If it is, return the number itself as the largest prime factor.

4. If the input number is not prime, use the `prime_factors` function to find all its prime factors. Sort the list of prime factors in descending order.

5. Return the last element of the sorted list, which will be the largest prime factor of the input number.

Here's the code that implements the solution:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    i = 2
    factors = []
    while n % i != 0:
        i += 1
    factors.append(i)
    while n > 1:
        n //= i
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def largest_prime_factor(n):
    if is_prime(n):
        return n
    factors = prime_factors(n)
    return max(factors)
```

You can use the `largest_prime_factor` function to find the largest prime factor of any given number. For example, `largest_prime_factor(13195)` returns `29` and `larg