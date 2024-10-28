def sum_Of_Subarray_Prod(nums: list):
    n = len(nums)
    result = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            result += prod
    return result