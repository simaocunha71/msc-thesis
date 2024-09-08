
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

"""
Explanation:

The function uses Binary Search to find the first occurrence of a given number in a sorted array.

If the middle element of the array is equal to the target, we update the result to the current mid index and continue the search on the left half. This is because we want to find the first occurrence, so we might find a smaller index on the left half.

If the middle element is less than the target, we know the target must be in the right half of the array, so we update left to mid + 1.

If the middle element is greater than the target, we know the target must be in the left half of the array, so we update right to mid - 1.

At the end, we return the result. If the target was not found, result will be -1.
"""
<jupyter_output>
1
<jupyter_text>
Question 5
<jupyter_code>
