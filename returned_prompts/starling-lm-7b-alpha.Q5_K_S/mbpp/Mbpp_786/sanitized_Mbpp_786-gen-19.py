def right_insertion(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left