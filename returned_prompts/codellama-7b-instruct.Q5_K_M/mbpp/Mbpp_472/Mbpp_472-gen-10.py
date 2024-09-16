def check_Consecutive(arr):
    n = len(arr)
    if n == 0:
        return False
    for i in range(n-1):
        if arr[i+1]-arr[i] != 1:
            return False
    return True
