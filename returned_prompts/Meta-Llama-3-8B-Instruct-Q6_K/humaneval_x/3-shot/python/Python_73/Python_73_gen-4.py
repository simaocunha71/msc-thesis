    arr = arr[:]
    changes = 0
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            changes += 1
            arr[j] = arr[i]
        i += 1
        j -= 1
    return changes


