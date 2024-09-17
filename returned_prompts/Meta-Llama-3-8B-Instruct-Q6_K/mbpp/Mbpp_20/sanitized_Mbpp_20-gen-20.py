def is_woodall(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    for p in range(2, int(n**0.5) + 1):
        if is_prime(p) and n == 2**p * 2**(p-1) + 1:
            return True
    return False