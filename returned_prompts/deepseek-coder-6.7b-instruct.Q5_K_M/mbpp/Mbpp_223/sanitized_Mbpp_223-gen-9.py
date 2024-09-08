def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            if arr.count(x) > n // 2:
                return True
            else:
                return False
    return False