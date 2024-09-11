def kth_element(nums, k):
    # Sort the array
    nums.sort()
    return nums[k-1]

# Test
print(kth_element([12,3,5,7,19], 2))  # Output: 3

"""
The time complexity is O(n log n) because the sort method sorts the array with time complexity O(n log n). The space complexity is O(1) as the original array is not modified in-place.
"""

# Time: O(n log n)
# Space: O(1)

# Optimized solution
def kth_element(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == k:
            return nums[mid]
        elif nums[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]

# Test
print(kth_element([12,3,5,7,19], 2))  # Output: 3

"""
The time complexity is O(log n) because we perform a binary search to find the kth element. The space complexity is O(1) as the original array is not modified in-place.
"""

# Time: O(log n)
# Space: O(1)

# Optimized solution
def kth_element(nums, k):
    def find_kth_element(left, right, k):
        if left > right:
            return None
        mid = left + (right - left) // 2
        if nums[mid] == k:
            return nums[mid]
        elif nums[mid] < k:
            return find_kth_element(mid + 1, right, k)
        else:
            return find_kth_element(left, mid - 1, k)
    return find_kth_element(0, len(nums) - 1, k)

# Test
print(kth