    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            if n == 1:
                return a
            n -= 1
        if n == 0:
            return b
        if b > 10 ** 6:
            return "Number too large"
    return "Not enough prime Fibonacci numbers found"
    # or raise Exception("Not enough prime Fibonacci numbers found")


