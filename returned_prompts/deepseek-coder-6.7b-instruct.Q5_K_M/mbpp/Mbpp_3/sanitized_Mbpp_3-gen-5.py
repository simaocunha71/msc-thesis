def is_not_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    return False