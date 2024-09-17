def search(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]