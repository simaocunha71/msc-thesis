def odd_length_sum(nums):
    total_sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            subarray = nums[i:j]
            if len(subarray) % 2 != 0:
                total_sum += sum(subarray)
    return total_sum