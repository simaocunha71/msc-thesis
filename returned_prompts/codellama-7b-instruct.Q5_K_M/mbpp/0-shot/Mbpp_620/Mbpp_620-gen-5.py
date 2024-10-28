"""
def largest_subset(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def divisible(a, b):
        return a % b == 0

    nums.sort()
    i = 0
    while i < len(nums):
        if not divisible(nums[i], nums[i+1]):
            return i + 1
        i += 1
    return len(nums)
"""
