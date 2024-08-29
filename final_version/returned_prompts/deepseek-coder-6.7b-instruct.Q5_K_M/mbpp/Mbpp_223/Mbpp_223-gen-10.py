def is_majority(arr, n, x):
    # First check if element x is present at n/2 or more times
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    if count > n // 2:
        return True
    else:
        return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))  # Returns: True


"""
Time complexity of this approach is O(n) and auxiliary space used is O(1).
"""


"""
