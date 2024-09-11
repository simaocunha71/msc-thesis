import math
def sum_Of_Subarray_Prod(nums):
    sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum += math.prod(nums[i:j+1])
    return sum