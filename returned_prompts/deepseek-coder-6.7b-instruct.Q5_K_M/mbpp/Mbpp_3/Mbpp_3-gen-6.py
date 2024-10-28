
def is_not_prime(n):
    if n == 2:
        return False
    if n % 2 == 0 or n <= 1:
        return True

    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return True
    return False

assert is_not_prime(2) == False
assert is_not_prime(4) == True
assert is_not_prime(6) == True
assert is_not_prime(8) == True
assert is_not_prime(10) == True
assert is_not_prime(12) == True
assert is_not_prime(14) == True
assert is_not_prime(16) == True
assert is_not_prime(18) == True
assert is_not_prime(20) == True
assert is_not_prime(22) == True
assert is_not_prime(24) == True
assert is_not_prime(26) == True
assert is_not_prime(28) == True
assert is_not_prime(30) == True
assert is_not_prime(32) == True
assert is_not_prime(34) == True
assert is_not_prime(36) == True
assert is_not_prime(38) == True
assert is_not_prime(40) == True
assert is_not_prime(42) == True
assert is_not_prime(44) == True
assert is_not_prime(46) == True
assert is_not_prime(48) == True
assert is_not_prime(50) == True
assert is_not_prime(52) == True
assert is_not_prime(54) == True
assert is_not_prime(56) == True
assert is_not_prime(58) == True
assert is_not_prime(60) == True
assert is_not_prime(62) == True
assert is_not_prime(64) == True
assert is_not_prime(66