def two_unique_nums(nums):
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    return [num for num, count in count_dict.items() if count == 1]