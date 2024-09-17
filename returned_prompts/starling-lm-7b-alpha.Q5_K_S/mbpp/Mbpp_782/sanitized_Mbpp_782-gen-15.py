def odd_length_sum(nums):
    s = 0
    for i in range(len(nums)):
        s += (i+1)*nums[i]
    return s