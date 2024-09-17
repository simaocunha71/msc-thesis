def kth_element(nums, k):
    if k > len(nums): return None
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= nums[k - 1]:
            right = mid - 1
        else:
            left = mid + 1
    return nums[left]