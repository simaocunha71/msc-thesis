def find_first_occurrence(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1