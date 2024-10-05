    n = len(arr)
    i = 0
    j = n - 1
    changes = 0

    while i < j:
        if arr[i] != arr[j]:
            changes += 1
            if arr[i] < arr[j]:
                arr[j] = arr[i]
            else:
                arr[i] = arr[j]
        i += 1
        j -= 1

    return changes

