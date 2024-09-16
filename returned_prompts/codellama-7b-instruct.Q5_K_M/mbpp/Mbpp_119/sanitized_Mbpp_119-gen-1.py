def search(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[right]:
            right = mid - 1
        elif arr[mid] == arr[left]:
            left = mid + 1
        else:
            return arr[mid]
    return arr[left] if arr[left] != arr[right] else arr[right]