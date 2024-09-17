def largest_subset(nums):
    return len(filter(lambda x: x % gcd(nums) == 0, nums))