
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    i, count = 1, 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1
    return fib(i - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This code defines two helper functions: `is_prime` which checks if a number is prime, and `fib` which computes the n-th Fibonacci number. The main function `prime_fib` then iterates over Fibonacci numbers, checking if each one is prime, and if it is, it increments a counter. When the counter reaches the desired number, it returns the last Fibonacci number it checked.

This code is correct and efficient, but it may be slow for large inputs because it checks each Fibonacci number and its primality. It's also possible to improve the primality check by storing already-checked numbers and using them to quickly determine if a number is prime. However, this would make the code more complex.

Please note that the `doctest` module is used to validate the code. It checks if the output of the function matches the expected output in the comments at the end of the function. If the function is correct, it should pass all the tests.

Also, note that the function `prime_fib` is not guaranteed to work for negative inputs or zero, because prime numbers are defined as being greater than 1, and Fibonacci numbers are defined as starting with 0 and 1.

Finally, remember that this code uses a naive primality test that's suitable for small inputs. For larger inputs, a more efficient primality test would be necessary.
"""

# 