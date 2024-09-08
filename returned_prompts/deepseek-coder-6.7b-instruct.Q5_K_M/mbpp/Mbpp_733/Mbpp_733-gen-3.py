def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))

# Time complexity: O(logn)
# Space complexity: O(1)

# In this problem, we are asked to find the first occurrence of a number in a sorted array. 
# We can use binary search, which reduces the search space by half in each step, hence the time complexity is O(logn). 
# The binary search process does not use any extra space, so the space complexity is O(1).
<jupyter_output>
1
<jupyter_text>
4. Find the Smallest Letter Greater Than Target
<jupyter_code>
