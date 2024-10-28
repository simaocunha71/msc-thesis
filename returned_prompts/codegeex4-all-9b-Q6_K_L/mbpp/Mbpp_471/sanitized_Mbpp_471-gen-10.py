def find_remainder(arr,n):
    prod = 1
    for num in arr:
        prod = (prod * num) % n
    return prod