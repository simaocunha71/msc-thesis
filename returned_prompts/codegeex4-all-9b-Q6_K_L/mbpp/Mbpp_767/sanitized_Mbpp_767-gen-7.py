def get_pairs_count(nums, sum):
    count = 0
    num_dict = {}
    for num in nums:
        if num in num_dict:
            count += num_dict[num]
        num_dict[sum - num] = num_dict.get(sum - num, 0) + 1
    return count