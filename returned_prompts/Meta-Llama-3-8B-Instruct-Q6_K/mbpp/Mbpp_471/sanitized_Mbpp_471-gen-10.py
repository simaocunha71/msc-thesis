def find_remainder(arr,n):
    res = 1
    for num in arr:
        res = (res * num) % n
    return res