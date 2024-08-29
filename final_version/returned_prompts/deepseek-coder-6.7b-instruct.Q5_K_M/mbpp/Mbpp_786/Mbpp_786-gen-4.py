def right_insertion(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(right_insertion([1,2,4,5],6))

#Output: 4

Explanation:
The function uses a binary search approach to find the right insertion point in the sorted list. If the target value is larger than the middle element, it sets the left boundary to be the middle plus one. If the target is smaller, it sets the right boundary to be the middle. This continues until the left boundary equals the right boundary. The left boundary will be the right insertion point.

Please note that this function assumes that the input list is sorted in ascending order.
"""

# 2. Binary Search
"""
