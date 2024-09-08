def get_pairs_count(nums, target_sum):
    count = 0
    nums_set = set(nums)
    for num in nums:
        if target_sum - num in nums_set:
            count += 1
    return count