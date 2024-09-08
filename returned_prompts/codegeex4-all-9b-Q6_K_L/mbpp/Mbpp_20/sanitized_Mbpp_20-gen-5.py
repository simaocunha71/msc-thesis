def is_woodall(n):
    def phi(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_woodall(n):
        if n < 2:
            return False
        p = 2
        while p * p <= n:
            if n % p == 0:
                return False
            p += 1
        if n > 1 and not is_prime(n):
            return False
        return phi(n) == n - 1

    return is_woodall(n)