def find_first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

# Using Binary Search
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            res = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

# Using Python's built-in function
def find_first_occurrence(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

# Using Python's built-in function bisect_left
from bisect import bisect_left

def find_first_occurrence(arr, target):
    idx = bisect_left(arr, target)
    if idx != len(arr) and arr[idx] == target:
        return idx
    return -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

# Using Python's built-in function bisect_right
from bisect import bisect_right

def find_