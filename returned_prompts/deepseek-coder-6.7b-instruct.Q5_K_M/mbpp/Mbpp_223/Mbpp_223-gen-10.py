
def is_majority(arr, n, x):
    i = 0
    while i < n:
        if arr[i] == x:
            break
        i += 1
    if i == n:
        return False
    if ((i + n//2) < n and arr[i + n//2] != x):
        return False
    return True


