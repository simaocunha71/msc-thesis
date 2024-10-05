
Here's a solution using a while loop and a for loop:

```python
from math import sqrt

def largest_prime_factor(n: int):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n
```

Explanation:

The `largest_prime_factor` function takes an integer `n` as input and returns the largest prime factor of `n`. It uses a while loop to iterate from 2 to the square root of `n`. Inside the loop, it checks if `n` is divisible by `i` using the modulo operator (`%`). If `n` is divisible by `i`, it divides `n` by `i` using the floor division operator (`//`) and continues the loop. If `n` is not divisible by `i`, it increments `i` by 1 and continues the loop. Once the loop ends, the function returns the value of `n`, which is the largest prime factor of the original input.

In the given example, `largest_prime_factor(13195)` returns 29 because 13195 is divisible by 29, but not by any smaller prime numbers. Similarly, `largest_prime_factor(2048)` returns 2 because 2048 is divisible by 2, but not by any smaller prime numbers.

Note that this solution assumes that `n` is greater than 1 and is not a prime number. It also uses the `sqrt` function from the `math` module to calculate the square root of `n`.

I hope this helps! Let me know if you have any more questions.

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```