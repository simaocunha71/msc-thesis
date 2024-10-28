def count_Pairs(nums, k):
    if k <= 0:
        return 0
    count = 0
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for key in num_dict:
        if key in num_dict:
            count += num_dict[key] * (num_dict[key] - 1) // 2
    return count