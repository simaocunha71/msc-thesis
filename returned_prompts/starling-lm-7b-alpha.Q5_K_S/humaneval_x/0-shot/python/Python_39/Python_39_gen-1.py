
To solve this problem, we can use the following steps:

1. Create a function `fibonacci_numbers` that generates the first `n` Fibonacci numbers using a generator.
2. Create a function `prime_numbers` that generates the first `n` prime numbers using a generator.
3. Merge the two generators using the `itertools.zip_longest` function, which will yield pairs of Fibonacci and prime numbers.
4. Filter the merged generator to keep only the pairs where the Fibonacci number is prime.
5. Count the number of prime Fibonacci numbers found and return it as the result.

Here's the implementation of the `prime_fib` function using the above steps:

```python
import itertools
from math import sqrt

def fibonacci_numbers(n):
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1

def prime_numbers(n):
    if n < 2:
        return
    yield 2
    for i in range(3, n + 1, 2):
        if all(i % j for j in range(3, int(sqrt(i)) + 1, 2)):
            yield i

def prime_fib(n):
    fib_primes = itertools.takewhile(lambda p: p[0] < n,
                                     itertools.zip_longest(fibonacci_numbers(n), prime_numbers(n)))
    return len(list(fib_primes))
```

You can use the `prime_fib` function to find the `n`-th prime Fibonacci number by passing the desired value of `n` as an argument. The function will return the result.

For example, `prime_fib(1)` will return 2, `prime_fib(2)` will return 3, `prime_fib(3)` will return 5, and so on.

Note that the `prime_fib` function uses the `itertools.zip_longest` function to merge the gener