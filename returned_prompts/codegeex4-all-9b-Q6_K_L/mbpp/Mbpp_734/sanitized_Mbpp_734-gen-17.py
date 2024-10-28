def sum_Of_Subarray_Prod(nums: list) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        temp = 1
        for j in range(i, n):
            temp *= nums[j]
            res += temp
    return res