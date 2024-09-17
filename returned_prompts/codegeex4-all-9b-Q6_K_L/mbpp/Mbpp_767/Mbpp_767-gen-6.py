def get_pairs_count(nums, sum):
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1

    pair_count = 0
    for num in nums_count:
        if sum - num in nums_count:
            if sum - num == num:
                pair_count += (nums_count[num] * (nums_count[num] - 1)) // 2
            else:
                pair_count += (nums_count[num] * nums_count[sum - num])

    return pair_count