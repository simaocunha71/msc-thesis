from math import sqrt
def count_Primes_nums(n):
    if n == 0:
        return 0
    else:
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True