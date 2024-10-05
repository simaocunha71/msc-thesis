
To solve this problem, you can use the Sieve of Eratosthenes algorithm to find all prime numbers up to the square root of `n`. Then, you can use trial division to find the largest prime factor of `n`. Here's a step-by-step guide on how to do this:

1. Create a boolean array called "prime" and set all entries to `True`. This array will be used to keep track of whether each number is prime or not.

2. Starting from 2, iterate through all numbers up to the square root of `n` (inclusive). For each number, mark it as non-prime if it is divisible by any number less than it. This process is known as "marking" the number.

3. After all numbers have been marked, iterate through the "prime" array again. If a number is marked as "True", it is a prime number. Add these numbers to a list called "primes".

4. Initialize a variable called "largest_prime" with a value of -1. This variable will store the largest prime factor of `n`.

5. Iterate through the "primes" list. For each prime number, check if `n` is divisible by the prime number. If it is, update the "largest_prime" variable with the value of the prime number.

6. Finally, return the "largest_prime" variable, which will be the largest prime factor of `n`.

Here's an implementation of the solution in Python:

```python
def largest_prime_factor(n: int):
    # Step 1: Create a boolean array called "prime" and set all entries to True.
    prime = [True] * (n + 1)

    # Step 2: Iterate through all numbers up to the square root of `n`.
    for i in range(2, int(n**0.5) + 1):
        # Step 2.1: Mark the number as non-prime if it is divisible by any number less than it.
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    # Step 3: Initialize a variable called "largest_prime