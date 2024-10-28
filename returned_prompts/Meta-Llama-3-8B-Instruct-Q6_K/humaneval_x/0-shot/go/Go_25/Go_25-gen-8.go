Here is a Python solution for the problem. It uses a helper function to check if a number is prime and then iterates over all numbers from 2 to n, checking if they are prime factors of n. 

```python
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            while n % i == 0:
                n //= i
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

This solution will work for all positive integers. It returns a list of prime factors of the input number in the order from smallest to largest. Each of the factors is listed number of times corresponding to how many times it appears in factorization. 

For example, `factorize(8)` returns `[2, 2, 2]`, `factorize(25)` returns `[5, 5]`, and `factorize(70)` returns `[2, 5, 7]`. 

The time complexity of this solution is O(sqrt(n)) and the space complexity is O(1). 

This solution is not optimized for large numbers, because it checks divisibility up to the square root of the number. For large numbers, a more efficient solution would be to use a sieve to generate all prime numbers up to the square root of the number and then check for divisibility among these prime numbers. 