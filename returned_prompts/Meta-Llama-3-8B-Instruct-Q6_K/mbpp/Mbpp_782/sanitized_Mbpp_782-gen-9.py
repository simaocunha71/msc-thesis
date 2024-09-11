def odd_length_sum(nums):
    total_sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if (j-i)%2 == 1:
                total_sum += sum(nums[i:j])
    return total_sum