def sum_Of_Subarray_Prod(nums):
    s = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j + 1]
            prod = 1
            for num in subarray:
                prod *= num
            s += prod
    return s