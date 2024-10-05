```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(2, a + 1):
        if is_prime(i):
            primes.append(i)

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
```
The function `is_multiply_prime(a)` checks if the given number `a` is the multiplication of 3 prime numbers. It first defines a helper function `is_prime(n)` to check if a number `n` is prime. Then it generates all prime numbers up to `a` and checks all possible combinations of 3 prime numbers to see if their multiplication is equal to `a`. If it finds such a combination, it returns `True`; otherwise, it returns `False`. 

This function can be optimized by only checking combinations of prime numbers that are less than or equal to the square root of `a`, since a larger factor of the number would be a multiple of a smaller factor that has already been checked. 

The time complexity of this function is O(n^2), where n is the number of prime numbers up to `a`. This is because it has to check all possible combinations of 3 prime numbers. The space complexity is O(n), where n is the number of prime numbers up to `a`, since it has to store all prime numbers in a list. 

This function can be further optimized by using a more efficient algorithm to generate prime numbers, such as the Sieve of Eratosthenes algorithm, which has a time complexity of O(n log log n). However, this would make the code more complex and harder to understand. 

For example, the function `is_multiply_prime(30)` returns `True`, because 30 can be expressed as the multiplication of 3 prime numbers: 2 * 3 * 5. 

Note that this function only works for numbers less than 100, as specified in the problem. For larger numbers, it would be more efficient to use a more efficient algorithm to generate prime numbers, such as the Sieve of Er