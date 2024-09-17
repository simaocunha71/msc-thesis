def consecutive_duplicates(nums: list):
    result = []
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            result.append(nums[i])
    result.append(nums[-1])
    return result