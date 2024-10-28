def is_multiply_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(2, a+1) if is_prime(num)]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False

print(is_multiply_prime(30))  # True
print(is_multiply_prime(40))  # False
print(is_multiply_prime(50))  # False
print(is_multiply_prime(60))  # False
print(is_multiply_prime(70))  # False
print(is_multiply_prime(80))  # False
print(is_multiply_prime(90))  # False
print(is_multiply_prime(100))  # False