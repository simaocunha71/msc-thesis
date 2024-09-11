def search(nums):
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        return nums[i]
    return nums[-1] if len(nums) > 0 else None