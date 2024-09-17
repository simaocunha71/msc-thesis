def is_majority(arr, n, x):
    i =0
    while i<n:
        if arr[i] == x:
            break
        i += 1
    if i == n:
        return False
    if ((n // x) <= i) or ((n // x) + 1 <= (n - i)):
        return True
    return False