def is_majority(arr, n, target):
    if len(arr) != n:
        raise ValueError("Array length does not match the given n")
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left = mid + 1
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == n:
        return False
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid + 1 <= right and arr[mid + 1] == target:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left >= n // 2