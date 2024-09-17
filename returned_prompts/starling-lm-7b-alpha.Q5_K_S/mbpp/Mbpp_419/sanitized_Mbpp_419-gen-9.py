def round_and_sum(nums):
    total_sum = 0
    for num in nums:
        total_sum += round(num)
    return total_sum * len(nums)