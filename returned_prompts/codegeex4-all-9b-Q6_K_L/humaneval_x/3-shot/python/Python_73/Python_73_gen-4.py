    n = len(arr)
    left = 0
    right = n - 1
    changes = 0

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes