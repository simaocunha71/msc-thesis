def sum_Of_Subarray_Prod(nums):
    total_sum = 0
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            total_sum += prod
    return total_sum