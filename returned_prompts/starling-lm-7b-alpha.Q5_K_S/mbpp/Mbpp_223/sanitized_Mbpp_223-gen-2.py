def is_majority(arr, n, element):
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == element:
            break
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    count = 0

    for i in range(left, n):
        if arr[i] == element:
            count += 1

    return count > n // 2