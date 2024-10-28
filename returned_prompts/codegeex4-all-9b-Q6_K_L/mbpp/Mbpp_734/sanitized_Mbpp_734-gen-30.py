def sum_Of_Subarray_Prod(nums):
    length = len(nums)
    total_sum = 0
    for i in range(length):
        for j in range(i, length):
            subarray = nums[i:j+1]
            product = 1
            for num in subarray:
                product *= num
            total_sum += product
    return total_sum