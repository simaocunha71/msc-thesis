def find_missing(arr):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] - mid == 1:
            low = mid + 1
        else:
            high = mid
    return arr[low] - 1

print(find_missing([1,2,4,5]))
print(find_missing([1,2,3,4,6,7,8]))
<jupyter_output>
3
5
<jupyter_text>
Binary Search (Continued)
<jupyter_code>
#Q4:
"""
Given a sorted list of integers, write a function to find the first occurrence of a given number.
assert find_first_occurrence([1,2