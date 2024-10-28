def is_majority(arr, n, element):
    if n == 0:
        return False
    left = 0
    right = n - 1
    while left <= right:
        if arr[left] == element:
            left += 1
        if arr[right] == element:
            right -= 1
        if left > right:
            break
    return left == right