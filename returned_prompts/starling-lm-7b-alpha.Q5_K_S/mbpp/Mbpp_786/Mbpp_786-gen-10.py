
def right_insertion(nums: list, val: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left

