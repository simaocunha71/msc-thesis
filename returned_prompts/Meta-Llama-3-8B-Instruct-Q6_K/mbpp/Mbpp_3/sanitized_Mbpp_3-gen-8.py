def is_not_prime(n):
    if type(n) != int or n <= 1:
        raise ValueError("Input must be a positive integer")
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False