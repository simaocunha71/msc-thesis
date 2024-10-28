def is_polite(n):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    count = 0
    i = 1
    while count < n:
        if is_prime(i):
            count += 1
        i += 1
    return i