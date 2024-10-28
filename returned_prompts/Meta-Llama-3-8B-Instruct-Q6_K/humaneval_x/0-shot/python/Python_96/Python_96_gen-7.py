```
def count_up_to(n):
    if n < 1:
        return []

    primes = []
    i = 2
    while i < n:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1

    return primes
```


Python code that implements the function `count_up_to(n)`:

This function generates all prime numbers less than `n` and returns them as an array. It uses a simple trial division method to check if a number is prime.

Here's an explanation of how the function works:

1. If `n` is less than 1, the function returns an empty array because there are no prime numbers less than 0.
2. The function initializes an empty array `primes` to store the prime numbers.
3. The function starts a loop from 2 to `n-1`. For each number `i` in this range:
   - It checks if `i` is prime by iterating from 2 to the square root of `i` and checking if `i` is divisible by any of these numbers. If it is, `i` is not prime.
   - If `i` is prime, it adds `i` to the `primes` array.
4. Finally, the function returns the `primes` array.

The time complexity of this function is O(n sqrt(n)), where `n` is the input number. This is because for each number in the range from 2 to `n`, we are iterating up to the square root of `n`. The space complexity is O(n), because in the worst case, all numbers less than `n` could be prime.