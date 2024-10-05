def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in range(2, a+1) if is_prime(x)]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False

print(is_multiply_prime(30))  # True
print(is_multiply_prime(35))  # False
print(is_multiply_prime(100))  # False
print(is_multiply_prime(7))  # False
print(is_multiply_prime(6))  # False