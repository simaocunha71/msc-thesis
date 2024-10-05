
Here's a solution in Python:

```python
def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
```

Explanation:
The function `count_up_to` takes an integer `n` as input and returns a list of prime numbers that are less than `n`. 

The function initializes an empty list called `primes` to store the prime numbers. It then uses a `for` loop to iterate through all numbers from 2 to `n-1`. 

For each number `i`, it sets a boolean variable `is_prime` to True. It then uses another `for` loop to check if `i` is divisible by any number from 2 to the square root of `i`. If it is divisible by any of these numbers, it means that `i` is not a prime number, so the `is_prime` variable is set to False and the inner loop is broken. 

After the inner loop finishes, the function checks the value of `is_prime`. If it is still True, it means