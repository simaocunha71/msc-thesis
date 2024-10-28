```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def multiply_primes(n):
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i):
                for j in range(i, int(n**0.5) + 1):
                    if is_prime(j):
                        for k in range(j, int(n**0.5) + 1):
                            if is_prime(k) and i * j * k == n:
                                return True
        return False

    return multiply_primes(a)
```
This function works by first defining a helper function `is_prime` to check if a number is prime. Then it defines another helper function `multiply_primes` to check if a number can be written as the multiplication of 3 prime numbers. It does this by iterating over all possible combinations of prime numbers and checking if their product is equal to the input number. If it is, it returns True. If it doesn't find any such combination, it returns False. The main function `is_multiply_prime` simply calls `multiply_primes` with the input number. 

Note that this function may be slow for large input numbers, because it has to iterate over all possible combinations of prime numbers. This can be optimized by only iterating over prime numbers that are less than or equal to the square root of the input number. This is because a larger factor of the input number would be a multiple of a smaller factor that has already been checked. 

Also, the function may return False for numbers that are actually the multiplication of 3 prime numbers, if the prime numbers are too large. This is because the function only checks up to the square root of the input number for prime factors, and if the prime factors are larger than this, they will not be found. 

In practice, you would want to add some checks to make sure that the input number is a positive integer, and you might want to use a more efficient algorithm to find prime numbers. 

Here is an optimized version of the function:
```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1