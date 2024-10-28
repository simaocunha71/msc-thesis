
def find_first_occurrence(arr, x):
    # Find the first occurrence of x in arr[0..n-1]
    # If x is present in arr, then return its index
    # Else return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


