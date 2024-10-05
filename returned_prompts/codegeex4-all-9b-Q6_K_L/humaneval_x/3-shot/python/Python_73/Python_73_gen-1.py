    count = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            count += 1
            if arr[left] > arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
        left += 1
        right -= 1

    return count

