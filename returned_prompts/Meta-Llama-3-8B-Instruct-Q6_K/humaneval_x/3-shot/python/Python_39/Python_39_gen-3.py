    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    i = 0
    while True:
        a, b = b, a + b
        i += 1
        if is_prime(b):
            if i == n:
                return b
            else:
                continue
        else:
            continue


