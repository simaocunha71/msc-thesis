Here is the Python function that implements the problem statement:

```python
def count_up_to(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

In this function, we use a helper function `is_prime` to check if a number is prime. The `count_up_to` function iterates over all numbers from 2 to `n-1` and checks if they are prime using the `is_prime` function. If a number is prime, it is added to the result list. The function finally returns the list of prime numbers.

For example, calling `count_up_to(5)` will return `[2, 3]`, which are the first two prime numbers less than 5. Similarly, calling `count_up_to(11)` will return `[2, 3, 5, 7]`, which are the first four prime numbers less than 11. If `n` is 0 or 1, the function returns an empty list. If `n` is larger than 2, the function returns a list of all prime numbers less than `n`. 