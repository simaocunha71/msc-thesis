def round_and_sum(nums):
    sum = 0
    for num in nums:
        sum += round(num)
    return sum