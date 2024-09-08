def right_insertion(arr, n):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if n < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low

print(right_insertion([1,2,4,5],6))

"""
Explanation:
The function uses binary search to find the right insertion point. If the value is less than the middle element, the high value is set to the middle. If the value is greater than or equal to the middle element, the low value is set to the middle plus one. This continues until the low value equals the high value, at which point the index of the right insertion point is returned.
"""
<jupyter_output>
4
<jupyter_text>
Question 3:
<jupyter_code>
