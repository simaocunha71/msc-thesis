"""
def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x and arr[i + n//2] == x:
            return True
    return False
"""

def is_majority(arr, n, x):
    mid = n // 2
    if arr[mid] == x:
        if mid == n - 1 or arr[mid + 1] != x:
            return True
        else:
            return arr[mid + mid//2] == x
    elif arr[mid] > x:
        return is_majority(arr[:mid], mid, x)
    else:
        return is_majority(arr[mid + 1:], n - mid - 1, x)

assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4) == False
assert is_majority([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], 13, 1) == True
assert is_majority([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], 13, 2) == True
assert is_majority([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], 13, 3) == False
assert is_majority([1], 1, 1) == True
assert is_majority([2], 1, 1) == False
assert is_majority([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10, 2) == False
assert is_majority([1, 1, 2, 2