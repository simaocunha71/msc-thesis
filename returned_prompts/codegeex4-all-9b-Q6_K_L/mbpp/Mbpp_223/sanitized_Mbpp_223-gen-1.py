def is_majority(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count > n // 2