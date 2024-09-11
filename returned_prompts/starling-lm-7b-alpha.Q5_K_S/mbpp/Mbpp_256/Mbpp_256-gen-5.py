"""
def count_Primes_nums(n):
    def is_prime(num):
        if num == 2:
            return True
        if num == 3:
            return True
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0:
                return False
            if num % (i + 2) == 0:
                return False
        return True

    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count
"""

