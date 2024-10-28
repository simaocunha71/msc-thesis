def is_not_prime(n):
    if n <= 1:
        return True
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return True
    return False

print(is_not_prime(2))  # False

