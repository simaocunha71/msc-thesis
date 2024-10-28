def zero_count(nums):
    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1
    return zero_count / len(nums)