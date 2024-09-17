def round_and_sum(nums):
    total = 0
    for num in nums:
        total += round(num)
    return total * len(nums)