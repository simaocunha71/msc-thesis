"""
def is_Monotonic(arr):
    n = len(arr)
    if n == 1:
        return True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
"""
