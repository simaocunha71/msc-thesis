def odd_length_sum(nums):
    sum_odd_length = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if (j-i) % 2 == 1:
                sum_odd_length += sum(nums[i:j])
    return sum_odd_length