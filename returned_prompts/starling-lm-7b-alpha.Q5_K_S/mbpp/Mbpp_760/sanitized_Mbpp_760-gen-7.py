def unique_Element(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return False
    return True
nums = [1, 1, 1]