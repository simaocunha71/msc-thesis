```
def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    p = 2
    while p * p < n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(1 for p in primes if p)
```



In this problem, we are asked to write a function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.

The function starts by checking if the input number is less than 2, in which case it returns 0 because there are no prime numbers less than 0 or 1.

Then, it creates a list of boolean values, `primes`, of size `n`, where `primes[i]` represents whether `i` is a prime number or not. It sets `primes[0]` and `primes[1]` to `False` because 0 and 1 are not prime numbers.

Next, it initializes a variable `p` to 2, which is the smallest prime number. It then enters a loop that continues until `p * p` is greater than or equal to `n`. In each iteration of the loop, it checks if `primes[p]` is `True`, which means `p` is a prime number. If `p` is a prime number, it sets all the multiples of `p` in the `primes` list to `False` because they are not prime numbers.

Finally, it returns the sum of all the `True` values in the `primes` list, which represents the number of prime numbers less than `n`. This is achieved using a generator expression `sum(1 for p in primes if p)`.

The unit test `assert count_Primes_nums(5) == 2` ensures that the function returns the correct result for the input 5. It checks if the function returns 2, which is the correct number of prime numbers less than 5 (2 and 3). If the function returns any other value, the test will fail.