def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x and arr[i + n//2] == x:
            return True
    return False