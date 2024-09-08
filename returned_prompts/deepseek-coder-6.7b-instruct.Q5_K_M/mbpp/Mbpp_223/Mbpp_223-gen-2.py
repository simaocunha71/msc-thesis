def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x and arr[i + n//2] == x:
            return True
    return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))  # True
print(is_majority([1, 2, 3, 4, 5, 6, 7], 7, 3))  # False
"""
Explanation:
In the first example, the element 3 is the majority element as it occurs 4 times which is more than n/2 = 7/2.
In the second example, no element occurs more than n/2 times in the given array. Therefore, the function should return False.
"""

# Method 2: Using Binary Search

def is_majority(arr, n, x):
    i = binary_search(arr, 0, n-1, x)
    if i == -1:
        return False
    if (i + n//2 < n) and arr[i + n//2] == x:
        return True
    return False

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, (mid - 1), x)
        else:
            return binary_search(arr, (mid + 1), high, x)
    else:
        return -1

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))  # True
print(is_majority([1, 2, 3, 4, 5, 6, 7], 7, 3))  # False

# Method 3: Using Two Pointer Approach

def is_majority(arr, n, x):
    i = 