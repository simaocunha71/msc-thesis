def is_majority(arr, n, element):
    cnt = 0
    for i in range(n):
        if arr[i] == element:
            cnt += 1
    return cnt > n // 2