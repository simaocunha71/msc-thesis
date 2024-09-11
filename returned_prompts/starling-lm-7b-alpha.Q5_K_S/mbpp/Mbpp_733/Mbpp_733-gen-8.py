def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low

# Test
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1)
"""
The above solution is incorrect.
Here's a correct solution:
"""

def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Test
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1)
"""
The above solution is incorrect.
Here's a correct solution:
"""

def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low if low < len(arr) and arr[low] == target else -1

# Test
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1)