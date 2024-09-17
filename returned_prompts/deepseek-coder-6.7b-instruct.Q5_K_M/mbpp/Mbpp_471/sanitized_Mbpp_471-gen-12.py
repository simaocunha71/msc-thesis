def find_remainder(arr,n):
    prod = 1
    for i in arr:
        prod = (prod * i) % n
    return prod % n