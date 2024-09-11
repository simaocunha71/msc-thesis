def get_pairs_count(nums, sum):
    nums_dict = {}
    pairs_count = 0
    for num in nums:
        if sum - num in nums_dict:
            pairs_count += nums_dict[sum - num]
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    return pairs_count