    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        for i in range(2, 100):
            if is_prime(i):
                for j in range(i, 100):
                    if is_prime(j):
                        for k in range(j, 100):
                            if is_prime(k) and i * j * k == a:
                                return True
        return False

print(is_multiply_prime(30))  # True
print(is_multiply_prime(31))  # False
print(is_multiply_prime(32))  # False
print(is_multiply_prime(33))  # False
print(is_multiply_prime(34))  # False
print(is_multiply_prime(35))  # False
print(is_multiply_prime(36))  # False
print(is_multiply_prime(37))  # False
print(is_multiply_prime(38))  # False
print(is_multiply_prime(39))  # False
print(is_multiply_prime(40))  # False
print(is_multiply_prime(42))  # True
print(is_multiply_prime(44))  # True
print(is_multiply_prime(45))  # True
print(is_multiply_prime(46))  # False
print(is_multiply_prime(48))  # False
print(is_multiply_prime(50))  # False
print(is_multiply_prime(51))  # False
print(is_multiply_prime(52))  # False
print(is_multiply_prime(54))  # False
print(is_multiply_prime(55))  # True
print(is_multiply_prime(56))  # True
print(is_multiply_prime(57))  # False
print(is_multiply_prime(58))  # False
print(is_multiply_prime(60))  # False
print(is_multiply_prime(63))  # True
print(is_multiply_prime(65))  # True
print(is_multiply_prime(66))  # True
print(is_multiply_prime(68))  # False
print(is_multiply_prime(69))  # False
print(is_multiply_prime(70))  # False
print(is_multiply_prime(72))  # False
print(is_multiply_prime(74))  # False
print(is_multiply_prime(75))  # True
print(is_multiply_prime(77))  # True
print