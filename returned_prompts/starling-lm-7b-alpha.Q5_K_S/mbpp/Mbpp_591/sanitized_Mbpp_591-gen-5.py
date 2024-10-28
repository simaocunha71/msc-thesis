def swap_List(nums):
    tmp = nums[0]
    nums[0] = nums[-1]
    nums[-1] = tmp
    return nums