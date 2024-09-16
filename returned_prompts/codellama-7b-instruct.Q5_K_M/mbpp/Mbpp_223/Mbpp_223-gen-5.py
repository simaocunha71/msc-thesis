def is_majority(arr, n, elem):
    cnt = 0
    for i in range(n):
        if arr[i] == elem:
            cnt += 1
            if cnt > n // 2:
                return True
    return False
