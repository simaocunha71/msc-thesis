def binary_search(arr, ele):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == ele:
            return (True, mid)
        elif arr[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    return (False, -1)

print(binary_search([11,23,31,43,56,58,65,77,12,19],31))

