    i, j = 0, len(arr) - 1
    count = 0
    while i < j:
        if arr[i] != arr[j]:
            count += 1
        i += 1
        j -= 1
    return count


