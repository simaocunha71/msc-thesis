def round_and_sum(nums):
    total = 0
    for n in nums:
        total += round(n)
    return total * len(nums)