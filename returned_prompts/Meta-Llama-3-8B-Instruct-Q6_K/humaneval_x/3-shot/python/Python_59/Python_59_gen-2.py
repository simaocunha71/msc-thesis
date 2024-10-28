    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    i = n // 2
    while i > 1:
        if n % i == 0 and is_prime(i):
            return i
        i -= 1
    return 2


