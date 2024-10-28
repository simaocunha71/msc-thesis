    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        for i in range(2, a):
            if is_prime(i):
                for j in range(i, a):
                    if is_prime(j):
                        for k in range(j, a):
                            if is_prime(k) and i * j * k == a:
                                return True
        return False

    print(is_multiply_prime(30))  # True
    print(is_multiply_prime(31))  # False
    print(is_multiply_prime(35))  # True
    print(is_multiply_prime(36))  # False
    print(is_multiply_prime(42))  # False
    print(is_multiply_prime(50))  # True
    print(is_multiply_prime(51))  # False
    print(is_multiply_prime(55))  # True
    print(is_multiply_prime(56))  # False
    print(is_multiply_prime(60))  # True
    print(is_multiply_prime(61))  # False
    print(is_multiply_prime(65))  # True
    print(is_multiply_prime(66))  # False
    print(is_multiply_prime(70))  # False
    print(is_multiply_prime(71))  # False
    print(is_multiply_prime(72))  # False
    print(is_multiply_prime(75))  # False
    print(is_multiply_prime(76))  # False
    print(is_multiply_prime(77))  # False
    print(is_multiply_prime(78))  # False
    print(is_multiply_prime(80))  # False
    print(is_multiply_prime(81))  # False
    print(is_multiply_prime(82))  # False
    print(is_multiply_prime(83))  # False
    print(is_multiply_prime(84))  # False
    print(is_multiply_prime(85))  # False
    print(is_multiply_prime(86))  # False
    print(is_multiply_prime(87))  # False
    print(is_multiply_prime(88))  # False
    print(is_multiply_prime(90))  # False
    print(is_multiply_prime(91))  # False
    print(is_multiply_prime(92))  # False
    print(is_multiply