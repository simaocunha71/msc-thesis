def largest_subset(nums):
    from functools import lru_cache
    @lru_cache(None)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    max_size = 0
    for i in range(len(nums)):
        size = 1
        for j in range(i + 1, len(nums)):
            if gcd(nums[i], nums[j]) == 1:
                size += 1
        max_size = max(max_size, size)
    return max_size