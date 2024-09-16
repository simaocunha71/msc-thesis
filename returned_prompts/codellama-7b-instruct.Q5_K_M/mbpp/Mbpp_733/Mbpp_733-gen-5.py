"""
def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
"""
