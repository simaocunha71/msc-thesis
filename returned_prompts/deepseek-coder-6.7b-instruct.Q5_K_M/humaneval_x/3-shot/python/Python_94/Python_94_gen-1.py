    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in lst if is_prime(x)]
    if primes:
        return sum(int(i) for i in str(max(primes)))
    else:
        return 0


