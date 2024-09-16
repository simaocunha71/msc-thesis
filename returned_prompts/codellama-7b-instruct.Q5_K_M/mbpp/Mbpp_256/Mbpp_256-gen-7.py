```
def count_Primes_nums(nums):
    if nums <= 2:
        return 0
    is_prime = [True] * (nums + 1)
    for i in range(2, int(nums ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, nums + 1, i):
                is_prime[j] = False
    return sum(is_prime[2:])
```
