    def is_prime(num: int) -> bool:
        """Check if given number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        """Return n-th number in Fibonacci sequence."""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    count = 0
    num = 0
    while True:
        if is_prime(fib(num)):
            count += 1
            if count == n:
                return fib(num)
        num += 1

