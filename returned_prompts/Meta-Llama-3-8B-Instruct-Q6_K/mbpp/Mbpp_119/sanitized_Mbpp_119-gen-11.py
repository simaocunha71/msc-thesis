def search(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[low]:
            low += 1
        elif nums[mid] == nums[high]:
            high -= 1
        else:
            return nums[mid]
    return nums[low]