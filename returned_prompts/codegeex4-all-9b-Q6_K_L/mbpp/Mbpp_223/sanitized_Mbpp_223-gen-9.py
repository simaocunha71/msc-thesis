def is_majority(arr, n, x):
    def binary_search(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    first = binary_search(arr, x)
    if first == -1:
        return False
    
    last = binary_search(arr, x)
    if last == -1:
        return False
    
    return (last - first + 1) > n // 2