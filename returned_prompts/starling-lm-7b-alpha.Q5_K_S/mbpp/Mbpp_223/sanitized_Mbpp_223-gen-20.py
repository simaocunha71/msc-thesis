def is_majority(arr, n, val):
    cnt = 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
    return cnt > n//2