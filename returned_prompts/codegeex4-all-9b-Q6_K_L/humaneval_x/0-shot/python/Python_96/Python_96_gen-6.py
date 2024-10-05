Here's one way to implement the `count_up_to` function:

```python
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
```

The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it's divisible by any of those numbers.

The `count_up_to` function then iterates from 2 to `n-1` and checks if each number is prime using the `is_prime` function. If it is, it adds it to the `primes` list.

Finally, the function returns the `primes` list.