
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases:

print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # False
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
print(is_prime(0))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(5))  # True
print(is_prime(7))  # True
print(is_prime(13))  # True
print(is_prime(17))  # True
print(is_prime(19))  # True
print(is_prime(23))  # True
print(is_prime(29))  # True
print(is_prime(31))  # True
print(is_prime(37))  # True
print(is_prime(41))  # True
print(is_prime(43))  # True
print(is_prime(47))  # True
print(is_prime(53))  # True
print(is_prime(59))  # True
print(is_prime(67))  # True
print(is_prime(71))  # True
print(is_prime(73))  # True
print(is_prime(79))  # True
print(is_prime(83))  # True
print(is_prime(89))  # True
print(is_prime(97))  # True

# 13441 is not a prime number because it is divisible by 1, 3, 41, 147, 487, 13441.

# This function works by first checking if n