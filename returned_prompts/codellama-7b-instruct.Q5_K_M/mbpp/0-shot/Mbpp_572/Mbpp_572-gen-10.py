def two_unique_nums(nums_list):
    # write your code here
    nums_list = sorted(nums_list)
    unique_nums = []
    for num in nums_list:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
