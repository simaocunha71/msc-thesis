def max_Abs_Diff(arr):
    return max(abs(arr[i] - arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)))

print(max_Abs_Diff((2,1,5,3))) # 4
"""
Explanation:
The maximum difference is between 5 (at index 2) and 3 (at index 3). The difference is 5 - 3 = 2.
"""

"""
This function works by first creating a list of all pairs of elements in the input array, then calculating the absolute difference for each pair. The max function is used to find the maximum difference in this list.
"""

# If you want the indices of the numbers that give you the maximum difference:

def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > max_diff:
                max_diff = abs(arr[i] - arr[j])
                indices = (i, j)
    return max_diff, indices

print(max_Abs_Diff((2,1,5,3))) # (4, (2, 3))

"""
Explanation:
The maximum difference is between 5 (at index 2) and 3 (at index 3). The difference is 5 - 3 = 2.
"""

# If you want to find the maximum difference between two numbers in the array without using any built-in functions:

def max_Abs_Diff(arr):
    min_val = arr[0]
    max_diff = 0
    for i in range(1, len(arr)):
        if arr[i] - min_val > max_diff:
            max_diff = arr[i] - min_val
        if arr[i] < min_val:
            min_val = arr[i]
    return max_diff

print(max_Abs_Diff((2,1,5,3))) # 4

"""
Explanation:
The maximum difference is between 5 (at index