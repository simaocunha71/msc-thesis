def max_sub_array_sum(nums, target):
    curr_sum = 0
    curr_max = float('-inf')
    for num in nums:
        curr_sum += num
        curr_max = max(curr_max, curr_sum)
        if curr_sum < target:
            curr_sum = 0
    return curr_max