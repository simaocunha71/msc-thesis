    n = len(arr)
    i = 0
    j = n - 1
    changes = 0

    while i < j:
        if arr[i] != arr[j]:
            changes += 1
        i += 1
        j -= 1

    return changes

