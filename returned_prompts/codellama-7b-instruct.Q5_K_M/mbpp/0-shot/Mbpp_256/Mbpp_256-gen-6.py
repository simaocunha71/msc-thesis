"""
def count_Primes_nums(nums):
    prime_count = 0
    for i in range(2, nums+1):
        if is_prime(i):
            prime_count += 1
    return prime_count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
"""
