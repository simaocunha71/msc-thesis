def is_not_prime(n):
    if n == 2:
        return False
    elif n < 2 or not all(n % i for i in range(2, int(n ** 0.5) + 1)):
        return True
    else:
        return False