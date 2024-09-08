def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            if arr.count(x) > n // 2:
                return True
            else:
                return False
    return False
"""
print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))
"""

# Solution:
def is_majority(arr, n, x):
    i = _binary_search(arr, 0, n, x)
    if i == -1:
        return False
    if arr[i + n//2] != x:
        return False
    return True

def _binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return _binary_search(arr, (mid + 1), high, x)
        else:
            return _binary_search(arr, low, (mid - 1), x)
    else:
        return -1

"""
print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3)) # should return True
"""

# Explanation:
# The function uses Binary search to find the first occurrence of the given element. If the element is found, it checks the element at index n/2 away. If it is the same as the given element, it means that the element occurs more than n/2 times, so returns True. Otherwise, it returns False.
# If the element is not found, it also returns False.
# This function runs in O(log n) time complexity.

# This is a more efficient solution as it uses binary search, which reduces the time complexity to O(log n), compared to the naive solution which runs in O(n) time.
<jupyter_output>
<empty_output>
<jupyter_text>
Question