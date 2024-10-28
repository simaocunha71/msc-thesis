def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(5))  # True
print(is_prime(7))  # True
print(is_prime(9))  # False
print(is_prime(10))  # False
print(is_prime(12))  # False
print(is_prime(15))  # False
print(is_prime(17))  # True
print(is_prime(19))  # True
print(is_prime(23))  # True
print(is_prime(25))  # False
print(is_prime(27))  # False
print(is_prime(30))  # False
print(is_prime(32))  # False
print(is_prime(33))  # False
print(is_prime(37))  # True
print(is_prime(39))  # False
print(is_prime(40))  # False
print(is_prime(43))  # True
print(is_prime(44))  # False
print(is_prime(46))  # False
print(is_prime(47))  # True
print(is_prime(48))  # False
print(is_prime(50))  # False
print(is_prime(51))  # False
print(is_prime(52))  # False
print(is_prime(53))  # True
print(is_prime(54))  # False
print(is_prime(55))  # False
print(is_prime(56))  # False
print(is_prime(57))  # False
print(is_prime(58))  # False
print(is_prime(59))  # True
print(is_prime(60))  # False
print(is_prime(61))  # True
print(is_prime(62))  # False
print(is_prime(63))  # False
print(is_prime(64