def newman_prime(n):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(n):
        while not is_prime(n):
            n += 1
        return n

    def newman_shanks_williams(n):
        if n == 1:
            return 2
        a = newman_shanks_williams(n // 2)
        b = next_prime(a ** 2 - 1)
        c = next_prime(a ** 2 + 1)
        return b if n % 2 == 0 else c

    return newman_shanks_williams(n)
