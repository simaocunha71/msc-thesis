def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if ((mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x):
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
def is_majority(arr, n, x):
    i = binary_search(arr, 0, n-1, x)
    if i == -1:
        return False
    if arr[i] != x:
        return False
    if i + n//2 < n and arr[i + n//2] == x:
        return True
    else:
        return False