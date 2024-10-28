def count_Primes_nums(nums):
    prime_nums = 0
    for i in range(2, nums + 1):
        if is_prime(i):
            prime_nums += 1
    return prime_nums
def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True