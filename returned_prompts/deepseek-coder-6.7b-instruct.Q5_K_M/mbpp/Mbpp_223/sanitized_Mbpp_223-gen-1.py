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