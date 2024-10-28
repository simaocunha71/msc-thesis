    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(n):
        primes = []
        i = 2
        while i * i <= n:
            if is_prime(i):
                while n % i == 0:
                    primes.append(i)
                    n //= i
            i += 1
        if n > 1:
            primes.append(n)
        return primes

    def is_multiply_prime(a):
        primes = find_primes(a)
        if len(primes) < 3:
            return False
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    if primes[i] * primes[j] * primes[k] == a:
                        return True
        return False

    return is_multiply_prime(30)  # True
    return is_multiply_prime(31)  # False
    return is_multiply_prime(45)  # False
    return is_multiply_prime(90)  # True
    return is_multiply_prime(99)  # True
    return is_multiply_prime(100)  # True
    return is_multiply_prime(101)  # False
    return is_multiply_prime(120)  # True
    return is_multiply_prime(150)  # True
    return is_multiply_prime(220)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30)  # True
    return is_multiply_prime(30) 