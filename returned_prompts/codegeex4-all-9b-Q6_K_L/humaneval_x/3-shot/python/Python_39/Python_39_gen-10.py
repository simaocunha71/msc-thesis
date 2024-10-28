    def is_prime(n: int) -> bool:
        """ Returns True if given number is prime, False otherwise. """
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def fib(n: int) -> int:
        """ Returns n-th Fibonacci number. """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    count = 0
    number = 2

    while True:
        if is_prime(number) and fib(number) == number:
            count += 1

        if count == n:
            return number

        number += 1

