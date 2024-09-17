def two_unique_nums(nums):
    nums.sort()
    unique_nums = []
    prev_num = None

    for num in nums:
        if num != prev_num:
            unique_nums.append(num)
            prev_num = num

    return unique_nums