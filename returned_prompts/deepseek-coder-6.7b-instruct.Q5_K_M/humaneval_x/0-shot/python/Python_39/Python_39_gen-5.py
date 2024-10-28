
    def prime_fib(n: int):
        if n < 1:
            return

        def is_prime(num: int):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def fib(n: int):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a

        count = 0
        i = 1
        while count < n:
            if is_prime(fib(i)):
                count += 1
            i += 1

        return fib(i - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


The function `prime_fib(n)` calculates the n-th Fibonacci number that is also prime. The function `is_prime(num)` checks if a number is prime, while `fib(n)` calculates the n-th Fibonacci number. The function iterates over the Fibonacci numbers, checking if each is prime and counting the primes it finds. When the count reaches `n`, the function returns the last Fibonacci number that was found to be prime.

Note: The function assumes that `n` is a positive integer. If `n` is not a positive integer, the function returns `None`.
"""

# 