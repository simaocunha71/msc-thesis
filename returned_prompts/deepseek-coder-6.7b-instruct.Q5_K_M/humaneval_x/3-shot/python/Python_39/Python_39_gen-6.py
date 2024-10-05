    def is_prime(num: int) -> bool:
        if num == 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b

    count = 0
    num = 1
    while True:
        if is_prime(fib(num)):
            count += 1
            if count == n:
                return fib(num)
        num += 1


