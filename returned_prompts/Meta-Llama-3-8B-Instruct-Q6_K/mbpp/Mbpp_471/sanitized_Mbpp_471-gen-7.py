def find_remainder(arr, n):
    res = 1
    for i in arr:
        res = (res * i) % n
    return res