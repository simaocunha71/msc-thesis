def is_majority(arr, n, elem):
    mid = n//2
    left = 0
    right = n-1
    while left < right:
        if arr[left] == elem:
            left += 1
        if arr[right] == elem:
            right -= 1
        if arr[left] != elem:
            right = left - 1
        if arr[right] != elem:
            left = right + 1
    return left > mid