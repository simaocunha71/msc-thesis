
To solve this problem, we can follow these steps:

1. Start with the largest possible factor of n, which is n itself.
2. Check if n is prime. If it is, return n as the largest prime factor. If not, continue to step 3.
3. Divide n by the largest prime factor found so far and update the largest prime factor if a larger one is found. Repeat this step until n can no longer be divided evenly by any prime number.
4. Return the largest prime factor found.

Here's a Python function that implements these steps:

```python
def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

In this function, we start with the smallest prime number, 2, and iterate up to the square root of n. For each prime number, we check if n is divisible by it. If not, we increment i by 1 and continue to the next prime number. If n is divisible by the current prime number, we update n by dividing it by the prime number. This process continues until n can no longer be divided evenly by any prime number. The largest prime factor is then returned.

For example, if we call `largest_prime_factor(13195)`, the function will return 29, as 29 is the largest prime factor of 13195. Similarly, if we call `largest_prime_factor(2048)`, the function will return 2, as 2 is the largest prime factor of 2048.

This function works efficiently by only checking divisibility up to the square root of n, as any factor larger than the square root of n would have a corresponding factor smaller than the square root of n.

I hope this explanation helps you understand how the function works and how to use it to solve the problem. Let me know if you have any more questions!

```python
def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i:
            i += 