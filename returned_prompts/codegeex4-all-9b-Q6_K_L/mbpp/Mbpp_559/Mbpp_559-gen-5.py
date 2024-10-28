def max_sub_array_sum(nums, k: int):
    max_sum = float('-inf')
    for i in range(len(nums) - k + 1):
        subarray_sum = sum(nums[i:i+k])
        max_sum = max(max_sum, subarray_sum)
    return max_sum

