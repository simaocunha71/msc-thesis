```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, 100):
        if is_prime(i) and a % i == 0:
            for j in range(i, 100):
                if is_prime(j) and a % j == 0:
                    for k in range(j, 100):
                        if is_prime(k) and a % k == 0:
                            return True
    return False
```
In this code, we first define a helper function `is_prime(n)` to check if a number is prime or not. Then, we iterate over all numbers from 2 to 100, and for each number, we check if it's prime and if it's a divisor of the given number `a`. If it is, we then iterate over the remaining numbers to find the other two prime divisors. If we find such a combination, we return `True`. If we don't find any combination, we return `False`. 

This code is not very efficient, as it checks all combinations of prime numbers. A more efficient solution would be to use a prime factorization algorithm to find the prime factors of `a`, and then check if there are exactly three prime factors. However, this is a more complex problem and would require a more advanced algorithm. 

The code above may take a long time to run for large inputs, because it checks all combinations of prime numbers. If you need a more efficient solution, you may want to consider using a prime factorization algorithm. 

For example, you can use the following code to find the prime factors of `a`:
```
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```
Then, you can check if the length of the list of prime factors is exactly 3:
```
def is_multiply_prime(a):
    factors = prime_factors(a)
    return len(factors) == 3
```
This code is much more efficient than the previous one, especially for large inputs.