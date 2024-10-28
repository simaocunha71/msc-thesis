def is_majority(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
        if count > n // 2:
            return True
    return False
