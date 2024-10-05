

def largest_prime_factor(n: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            largest_factor = i
            n //= i
            if n == 1:
                return largest_factor
    return largest_factor


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Python/math/largest_prime_factor_v2.py
