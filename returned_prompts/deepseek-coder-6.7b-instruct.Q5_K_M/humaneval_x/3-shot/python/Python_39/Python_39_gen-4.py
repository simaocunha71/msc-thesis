    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    count = 0
    i = 1
    while count < n:
        fib_number = fib(i)
        if is_prime(fib_number):
            count += 1
        i += 1

    return fib(i-1)


