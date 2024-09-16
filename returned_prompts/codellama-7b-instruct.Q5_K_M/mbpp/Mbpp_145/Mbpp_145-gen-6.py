"""
def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > max_diff:
                max_diff = abs(arr[i] - arr[j])
    return max_diff
"""































