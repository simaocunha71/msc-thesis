def search(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[mid - 1]:
            if (mid - left) % 2 == 0:
                left = mid + 1
            else:
                right = mid - 2
        elif arr[mid] == arr[mid + 1]:
            if (right - mid) % 2 == 0:
                right = mid - 1
            else:
                left = mid + 2
        else:
            return arr[mid]

    return arr[left]