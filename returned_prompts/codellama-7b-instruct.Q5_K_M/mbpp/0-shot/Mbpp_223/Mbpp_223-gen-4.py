def is_majority(arr, n, ele):
    if n == 0:
        return False
    left = 0
    right = n - 1
    while left < right:
        if arr[left] == ele:
            left += 1
        elif arr[right] == ele:
            right -= 1
        else:
            return False
    return left == right == (n - 1) // 2
