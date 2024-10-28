def is_not_prime(n):
    if n <= 1:
        return True
    elif n == 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

print(is_not_prime(2))  # False

