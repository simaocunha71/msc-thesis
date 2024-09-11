def get_Inv_Count(arr):
    n = len(arr)
    if n > 1:
        left = get_Inv_Count(arr[:n//2])
        right = get_Inv_Count(arr[n//2:])
        return left + right + merge_and_count(arr, n//2)
    return 0
def merge_and_count(arr, mid):
    inv_count = 0
    left = arr[:mid]
    right = arr[mid:]
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            inv_count += mid - i
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return inv_count