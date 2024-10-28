def last(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                left = mid + 1
    return -1