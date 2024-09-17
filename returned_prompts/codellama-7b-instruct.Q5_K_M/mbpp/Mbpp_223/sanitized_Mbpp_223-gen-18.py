def is_majority(arr, n, num):
    count = 0
    for i in range(n):
        if arr[i] == num:
            count += 1
        if count > n // 2:
            return True
    return False