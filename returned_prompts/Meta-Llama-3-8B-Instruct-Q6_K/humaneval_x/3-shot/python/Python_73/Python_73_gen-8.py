    arr = arr[::-1]
    changes = 0
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            changes += 1
    return changes


