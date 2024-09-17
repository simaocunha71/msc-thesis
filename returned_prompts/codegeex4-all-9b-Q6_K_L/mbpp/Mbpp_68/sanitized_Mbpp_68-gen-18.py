def is_Monotonic(nums):
    if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
        return True
    elif all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)):
        return True
    else:
        return False