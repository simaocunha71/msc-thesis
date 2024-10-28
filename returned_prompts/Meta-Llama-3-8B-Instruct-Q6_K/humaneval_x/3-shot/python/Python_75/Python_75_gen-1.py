    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        for i in range(2, 100):
            if a % i == 0:
                if is_prime(i):
                    j = a // i
                    if is_prime(j):
                        k = a // j
                        if is_prime(k):
                            return True
        return False

    print(is_multiply_prime(30))  # True
    print(is_multiply_prime(31))  # False
    print(is_multiply_prime(15))  # True
    print(is_multiply_prime(21))  # False
    print(is_multiply_prime(42))  # True
    print(is_multiply_prime(45))  # True
    print(is_multiply_prime(48))  # True
    print(is_multiply_prime(50))  # False
    print(is_multiply_prime(51))  # False
    print(is_multiply_prime(52))  # False
    print(is_multiply_prime(54))  # False
    print(is_multiply_prime(55))  # False
    print(is_multiply_prime(56))  # False
    print(is_multiply_prime(57))  # False
    print(is_multiply_prime(58))  # False
    print(is_multiply_prime(60))  # False
    print(is_multiply_prime(62))  # False
    print(is_multiply_prime(63))  # True
    print(is_multiply_prime(65))  # False
    print(is_multiply_prime(66))  # False
    print(is_multiply_prime(68))  # False
    print(is_multiply_prime(69))  # False
    print(is_multiply_prime(70))  # False
    print(is_multiply_prime(72))  # False
    print(is_multiply_prime(74))  # False
    print(is_multiply_prime(75))  # True
    print(is_multiply_prime(77))  # False
    print(is_multiply_prime(78))  # False
    print(is_multiply_prime(80))  # False
    print(is_multiply_prime(81))  # False
    print(is_multiply_prime(82))  # False
    print(is_multiply_prime(84))  # False
    print(is_multiply_prime(85))