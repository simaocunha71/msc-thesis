def search(nums):
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            return nums[i]
    return None