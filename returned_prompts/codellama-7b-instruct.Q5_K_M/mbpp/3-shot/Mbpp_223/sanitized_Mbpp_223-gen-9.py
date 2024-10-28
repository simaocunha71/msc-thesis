def is_majority(arr, n, elem):
    if n / 2 < 1:
        return False

    left = 0
    right = n - 1

    while left < right:
        if arr[left] == elem:
            left += 1
        else:
            right -= 1

    return left == right