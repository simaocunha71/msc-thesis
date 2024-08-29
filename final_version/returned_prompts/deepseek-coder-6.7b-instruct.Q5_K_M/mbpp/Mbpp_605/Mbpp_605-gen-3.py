def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test cases
print(prime_num(13))  # True
print(prime_num(14))  # False
print(prime_num(2))   # True
print(prime_num(1))   # False
print(prime_num(0))   # False
print(prime_num(-1))  # False


