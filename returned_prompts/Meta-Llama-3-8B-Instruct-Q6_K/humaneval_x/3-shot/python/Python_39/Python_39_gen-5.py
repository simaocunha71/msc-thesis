    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 2, 3
    count = 1

    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b


