    n = len(arr)
    left = 0
    right = n - 1
    changes = 0

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
            if arr[left] < arr[right]:
                arr[right] = arr[left]
            else:
                arr[left] = arr[right]
        left += 1
        right -= 1

    return changes

