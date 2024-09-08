def newman_prime(n):
    def newman(n):
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, b + c
        return a

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    count, i = 0, 1
    while count < n:
        num = newman(i)
        if is_prime(num):
            count += 1
        i += 1
    return num