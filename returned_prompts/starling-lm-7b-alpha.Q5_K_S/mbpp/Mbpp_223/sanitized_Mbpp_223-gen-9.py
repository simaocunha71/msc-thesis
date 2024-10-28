def is_majority(arr, n, e):
    i = 0
    while i < n:
        if arr[i] == e:
            i += 1
        else:
            return False
    return True