    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    i = 1
    while True:
        fib_number = fib(i)
        if is_prime(fib_number):
            n -= 1
            if n == 0:
                return fib_number
        i += 1


