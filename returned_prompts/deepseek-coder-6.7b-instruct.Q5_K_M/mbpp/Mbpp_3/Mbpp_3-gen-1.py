
def is_not_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False


assert is_not_prime(2) == False
assert is_not_prime(4) == True
assert is_not_prime(6) == True
assert is_not_prime(8) == True
assert is_not_prime(9) == True
assert is_not_prime(11) == False
assert is_not_prime(13) == False
assert is_not_prime(15) == True
assert is_not_prime(16) == True
assert is_not_prime(17) == False
assert is_not_prime(18) == True
assert is_not_prime(19) == False
assert is_not_prime(21) == True
assert is_not_prime(23) == False
assert is_not_prime(25) == True
assert is_not_prime(27) == True
assert is_not_prime(29) == False
assert is_not_prime(31) == False
assert is_not_prime(33) == True
assert is_not_prime(35) == True
assert is_not_prime(37) == False
assert is_not_prime(39) == True
assert is_not_prime(41) == False
assert is_not_prime(43) == False
assert is_not_prime(45) == True
assert is_not_prime(47) == False
assert is_not_prime(49) == True
assert is_not_prime(51) == True
assert is_not_prime(53) == False
assert is_not_prime(55) == True
assert is_not_prime(57) == True
assert is_not_prime(59) == False