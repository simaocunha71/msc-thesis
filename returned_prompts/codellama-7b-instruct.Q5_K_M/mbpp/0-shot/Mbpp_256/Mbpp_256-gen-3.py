```
def count_Primes_nums(nums):
    if nums <= 2:
        return 0
    prime_nums = []
    for i in range(2, nums):
        if is_prime(i):
            prime_nums.append(i)
    return len(prime_nums)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
