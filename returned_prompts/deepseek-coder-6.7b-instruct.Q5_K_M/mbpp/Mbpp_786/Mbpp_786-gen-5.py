def right_insertion(arr, n):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if n < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

print(right_insertion([1,2,4,5],6))  # Output: 4

Explanation:
The function uses binary search algorithm to find the right insertion point. If the target number is less than the middle element, it updates the right pointer to the middle. If the target number is greater or equal to the middle element, it updates the left pointer to the middle plus one. The loop continues until the left and right pointers meet, at which point the left pointer is the right insertion point.

"""

