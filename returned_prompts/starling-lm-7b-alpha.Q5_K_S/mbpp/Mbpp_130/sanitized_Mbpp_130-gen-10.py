def max_occurrences(nums):
    max_val = nums[0]
    max_count = 1
    for num in nums:
        if num == max_val:
            max_count += 1
        elif max_count < 1:
            max_val = num
            max_count = 1
        else:
            max_val = num
            max_count = 1
    return (max_val, max_count)