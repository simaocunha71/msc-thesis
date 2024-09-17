def two_unique_nums(nums_list):
    unique_nums = []
    for i in nums_list:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums