def search(nums):
    if len(nums) == 0:
        return None
    if len(set(nums)) != len(nums):
        return None
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]