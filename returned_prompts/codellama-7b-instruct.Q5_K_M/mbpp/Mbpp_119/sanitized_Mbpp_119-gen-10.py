def search(arr):
    if not arr: return None
    if len(arr) == 1: return arr[0]
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[mid - 1]:
            left = mid + 1
        else:
            right = mid
    return arr[left]