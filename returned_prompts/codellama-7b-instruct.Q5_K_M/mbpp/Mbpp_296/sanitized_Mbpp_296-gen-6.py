def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        inv_count = 0
        inv_count = inv_count + get_Inv_Count(left) + get_Inv_Count(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                inv_count = inv_count + (len(left) - i)
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