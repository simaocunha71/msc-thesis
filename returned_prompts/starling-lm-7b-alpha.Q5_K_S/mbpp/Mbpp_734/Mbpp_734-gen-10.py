
def sum_Of_Subarray_Prod(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return sum(sum_Of_Subarray_Prod(nums[1:]) + nums[0] * sum_Of_Subarray_Prod(nums[1:]))


