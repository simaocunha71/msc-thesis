
def prime_fib(n: int):
    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    while True:
        if is_prime(fib(n)):
            return fib(n)
        n += 1
