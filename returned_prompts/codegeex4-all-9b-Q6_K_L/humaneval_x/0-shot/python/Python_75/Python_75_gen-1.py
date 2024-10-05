def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in range(2, a + 1) if is_prime(x)]
    product = 1
    for prime in primes:
        product *= prime
        if product == a:
            return True
        elif product > a:
            return False
    return False

print(is_multiply_prime(30))  # True
print(is_multiply_prime(10))  # False
print(is_multiply_prime(50))  # False
print(is_multiply_prime(60))  # False
print(is_multiply_prime(70))  # False
print(is_multiply_prime(80))  # False
print(is_multiply_prime(90))  # False
print(is_multiply_prime(100))  # False
print(is_multiply_prime(110))  # False
print(is_multiply_prime(120))  # False
print(is_multiply_prime(130))  # False
print(is_multiply_prime(140))  # False
print(is_multiply_prime(150))  # False
print(is_multiply_prime(160))  # False
print(is_multiply_prime(170))  # False
print(is_multiply_prime(180))  # False
print(is_multiply_prime(190))  # False
print(is_multiply_prime(200))  # False
print(is_multiply_prime(210))  # False
print(is_multiply_prime(220))  # False
print(is_multiply_prime(230))  # False
print(is_multiply_prime(240))  # False
print(is_multiply_prime(250))  # False
print(is_multiply_prime(260))  # False
print(is_multiply_prime(270))  # False
print(is_multiply_prime(280))  # False
print(is_multiply_prime(290))  # False
print(is_multiply_prime(300))  # False
print(is_multiply_prime(310))  # False
print(is_multiply_prime(320))  # False
print(is_multiply_prime(330))  # False
print(is_multiply_prime(340))  # False
print(is_multiply_prime(350))  # False
print(is_multiply_prime(360))  # False
print(is_multiply_prime(370))  # False
print(is_multiply_prime(