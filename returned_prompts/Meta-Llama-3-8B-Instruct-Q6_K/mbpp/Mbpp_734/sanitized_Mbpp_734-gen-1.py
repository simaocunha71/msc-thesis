def sum_Of_Subarray_Prod(nums):
    n = len(nums)
    total_sum = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            total_sum += product
    return total_sum