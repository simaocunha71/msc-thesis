def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = get_Inv_Count(arr[:mid])
    right = get_Inv_Count(arr[mid:])
    inv_count = left + right
    i = j = k = 0
    while i < len(arr[:mid]) and j < len(arr[mid:]):
        if arr[i] <= arr[mid]:
            arr[k] = arr[i]
            i += 1
        else:
            arr[k] = arr[mid+j]
            j += 1
            inv_count += len(arr[:mid]) - i
        k += 1
    while i < len(arr[:mid]):
        arr[k] = arr[i]
        i += 1
        k += 1
    while j < len(arr[mid:]):
        arr[k] = arr[mid+j]
        j += 1
        k += 1
    return inv_count