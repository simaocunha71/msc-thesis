def max_sub_array_sum(nums, k):
    s = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if j - i + 1 == k:
                s += sum(nums[i:j+1])
    return s