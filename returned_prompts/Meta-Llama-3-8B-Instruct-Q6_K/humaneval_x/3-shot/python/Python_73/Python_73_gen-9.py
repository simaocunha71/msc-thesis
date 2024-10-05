    arr = arr.copy()
    n = len(arr)
    arr = arr + arr[::-1][1:]
    arr = list(set(arr))
    arr.sort()
    res = 0
    for i in range(n):
        if arr[i] != arr[n + i]:
            res += 1
    return res


