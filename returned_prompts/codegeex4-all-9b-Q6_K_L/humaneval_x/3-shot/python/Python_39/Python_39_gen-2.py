    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    count = 0
    i = 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1

    return fib(i - 1)

