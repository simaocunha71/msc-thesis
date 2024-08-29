
def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(nums) and nums[left] == target else -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))

# 3. Find Peak Element
