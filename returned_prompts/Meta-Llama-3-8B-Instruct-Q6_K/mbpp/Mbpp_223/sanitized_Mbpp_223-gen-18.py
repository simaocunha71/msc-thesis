def is_majority(arr, n, element):
    if n <= 0:
        return False
    if n == 1:
        return arr[0] == element
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            left, right = 0, mid
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return left < n and arr[left] == element