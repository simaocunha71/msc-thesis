
def is_majority(arr, n, x):
    i = 0
    while (i < n and arr[i] <= x):
        i += 1
    if (i + i > n or arr[i + i] != x):
        return False
    return True

