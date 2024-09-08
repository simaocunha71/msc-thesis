def left_insertion(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5], 6))

# Output: 4

"""
Explanation:
The function uses a binary search algorithm to find the target in the array. If the target is found, the index is returned immediately.
If the target is not found, the binary search will eventually narrow down to a single element (or zero elements). 
The left variable will be the insertion point for the target.
"""

# Time complexity: O(log n)
# Space complexity: O(1)
<jupyter_output>
4
<jupyter_text>
